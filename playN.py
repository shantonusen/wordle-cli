#!/usr/bin/env python3
import random
import sys
from datetime import datetime

import wordle
from cli import CLIPlayer

def print_help_exit():
    print("Usage: python3 play.py [-h|--help] [N] [--hints]")
    print()
    print("Option\t\t\tBehaviour (* = mutually-exclusive)")
    print("------\t\t\t----------------------------------")
    print("none\t\t\tUse a random solution from the official Wordle dictionary")
    print("N (number)\t\t* Create an N-way Wordle")
    print("--hints\t\t\tAfter each guess, report number of possible words remaining")
    print("-h, --help\t\tPrint this help text and quit")
    exit()

if __name__=="__main__":
    game = wordle.Game()
    player = CLIPlayer()

    fixed_solutions = None
    hints = False
    game_size = None
    for arg in sys.argv[1:]:
        if arg == "-h" or arg == "--help":
            print_help_exit()
        elif arg.isdigit() and int(arg) >= 0 and game_size == None:
            game_size = int(arg)
        elif arg == "--hints":
            hints = True
        else:
            player.warn(f"Invalid argument { arg }")
            print_help_exit()

    rounds = game_size + 5

    while True:
        fixed_solutions = random.sample(game.VALID_SOLUTIONS, game_size)
        try:
            game.play(player, fixed_solutions, hints=hints, rounds=rounds)
        except (KeyboardInterrupt, EOFError):
            print()
            player.quit()

        try:
            player.again()
            print()
        except (KeyboardInterrupt, EOFError):
            print()
            exit()
