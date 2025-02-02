import os
import platform
import shutil
import string
import subprocess
import sys
from configparser import ConfigParser
from typing import List

try:
    import readline
except ImportError:
    pass

from wordle import Game, LetterStates


class CLIConfig:
    RESET = "\x1b[0m"

    WARN = "\x1b[33m"
    WIN = "\x1b[1;32m"
    LOSE = "\x1b[1;31m"
    HI = "\x1b[1m"
    DIM = "\x1b[90m"
    STATE_COLOURS = {
        LetterStates.CORRECTPOSITION:    "\x1b[42;30m",
        LetterStates.INCORRECTPOSITION:  "\x1b[43;30m",
        LetterStates.NOTPRESENT:         "\x1b[40;37m",
        LetterStates.NOTGUESSEDYET:      "\x1b[90m"
        }
    SHARE_EMOJI = {
        LetterStates.CORRECTPOSITION:    "🟩",
        LetterStates.INCORRECTPOSITION:  "🟨",
        LetterStates.NOTPRESENT:         "⬛",
        LetterStates.NOTGUESSEDYET:      "⬜️"
        }

    # create new CLIConfig, loop through attributes and override values from config
    @staticmethod
    def from_ini(config_file="config.ini"):
        c = CLIConfig()
        parser = ConfigParser(comment_prefixes=("#"))
        if len(parser.read(os.path.join(os.path.dirname(__file__), config_file))) == 0:
            return c
        for attr in dir(c):
            if attr.startswith("__") or attr == "RESET" or not attr.isupper():
                continue
            elif isinstance(getattr(c, attr), dict) and parser.has_section(attr):
                for key in getattr(c, attr):
                    if parser.has_option(attr, str(key)):
                        getattr(c, attr)[key] = ("\x1b[{v}m" if attr == "STATE_COLOURS" else "{v}").format(v=parser.get(attr, str(key)))
            elif parser.has_option("COLOURS", attr):
                setattr(c, attr, "\x1b[{v}m".format(v=parser.get("COLOURS", attr)))
        return c

class CLIPlayer:
    ASSUME_GUESSES_VALID = False
    GAME_NUMBER = None
    _C : CLIConfig

    def __init__(self):
        self._lines_since_keyboard = -1
        self._response_history = []
        self._keyboard_status = {}
        try:
            self._C = CLIConfig.from_ini()
        except Exception as e:
            self._C = CLIConfig()
            self.warn(f"Exception parsing config file, using defaults instead ({ e })")

    def start(self):
        self._lines_since_keyboard = -1
        self._response_history = []
        self._keyboard_status = {letter: LetterStates.NOTGUESSEDYET for letter in string.ascii_uppercase}

        self.out(f"Let's play a game of Wordle")
        self.update_keyboard()

    def guess(self, round, out_of_rounds) -> str:
        prompt = "{:>13}".format(f"Guess { round }/{ out_of_rounds }: ")
        guess = input(prompt).upper()
        sys.stdout.write(f"\033[A\033[{len(prompt)}C\033[K") # move cursor up one line, right by len(prompt), then clear rest of line
        return guess

    def handle_response(self, guess: str, states_array: List[List[LetterStates]], hint: int):
        self._response_history.append((guess, states_array))
        for states in states_array:
            for letter, state in zip(guess, states):
                # only change a letter's keyboard status if new status is "better" (avoids repeat letter problem)
                if state.value > self._keyboard_status[letter].value:
                    self._keyboard_status[letter] = state
        self.out(self.pretty_response(guess, states_array, self._C)+(f" { self._C.DIM }{ hint } possible" if hint != -1 else ""))
        self.update_keyboard()

    def warn(self, warning):
        self.out(f"{ self._C.WARN }{ warning }")

    def handle_win(self, round, out_of_rounds):
        self.out(f"{ self._C.WIN }Got it in { round }/{ out_of_rounds } rounds")

        share_text = f"wordle-cli {(str(self.GAME_NUMBER)+' ' if self.GAME_NUMBER else '')}{round}/{out_of_rounds}\n"
        for _, states_array in self._response_history:
            share_text += "\n"
            share_line = ""
            for states in states_array:
                if len(share_line):
                    share_line += " "
                share_line += "".join(self._C.SHARE_EMOJI[state] for state in states)
            share_text += share_line

        if CLIPlayer.try_clipboard(share_text):
            self.out(f"📣 Shareable summary copied to clipboard")
        else:
            self.out(f"📣 Shareable summary:")
            self.out(share_text + "\n")

    def handle_loss(self, solutions):
        self.out(f"{ self._C.LOSE }🤦 LOSE! The solution was { ' '.join(solutions) }")

    def quit(self):
        self.out(f"{ self._C.LOSE }QUIT!")

    def again(self) -> str:
        return input(f"Play again { self._C.DIM }[Enter]{ self._C.RESET } or exit { self._C.DIM }[Ctrl-C]{ self._C.RESET }? ")

    def out(self, string=""):
        # print non-breaking space to avoid glitching on terminal resize
        print(f"{ string }{ self._C.RESET }\xA0")
        if self._lines_since_keyboard >= 1:
            self._lines_since_keyboard += 1

    def update_keyboard(self):
        if self._lines_since_keyboard >= 1:
            sys.stdout.write(f"\033[{self._lines_since_keyboard}F") # move cursor up to keyboard line
        sys.stdout.write(self.pretty_response(list(self._keyboard_status.keys()), [list(self._keyboard_status.values())], self._C)+"\xA0")
        if self._lines_since_keyboard >= 1:
            sys.stdout.write(f"\033[{self._lines_since_keyboard}E") # move cursor back down
        elif self._lines_since_keyboard == -1:
            sys.stdout.write("\n\n")
            self._lines_since_keyboard = 2

    # static method for use by other Player types
    @staticmethod
    def pretty_response(word, states_array, config: CLIConfig) -> str:
        outstr = ""
        for states in states_array:
            if len(outstr):
                outstr += " "
            outstr += "".join(f"{ config.STATE_COLOURS[state] }{ letter }{ config.RESET }" for letter, state in zip(word, states))
        return outstr

    @staticmethod
    def try_clipboard(text) -> bool:
        try:
            if hasattr(platform.uname(), "release") and "microsoft-standard" in platform.uname().release:
                clip = shutil.which("clip.exe") # WSL
            elif platform.system() == "Linux":
                clip = shutil.which("xclip") # untested!
            elif platform.system() == "Darwin":
                clip = shutil.which("pbcopy") # untested!
            if clip == None:
                return False
            p = subprocess.Popen(clip, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, env={'LANG': 'en_US.UTF-8'})
            p.communicate(input=text.encode('utf-8'))
            return p.returncode == 0
        except:
            return False
