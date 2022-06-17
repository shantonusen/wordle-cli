#!/usr/bin/env python3

# Determine a solution and guesses based on set of result rows

import os
import sys
from collections import Counter
import itertools

from wordle import Game, LetterStates

input_results = []
for input_result in sys.argv[1:]:
    if len(input_result) != Game.LENGTH:
        raise ValueError(f"{input_result} is not {Game.LENGTH} letters")

    input_result_states = []
    for input_result_char in input_result:
        if input_result_char == 'B':
            input_result_states.append(LetterStates.NOTPRESENT)
        elif input_result_char == 'Y':
            input_result_states.append(LetterStates.INCORRECTPOSITION)
        elif input_result_char == 'G':
            input_result_states.append(LetterStates.CORRECTPOSITION)
        else:
            raise ValueError(f"Unknown input result character {input_result_char} (not one of B=Not Present, Y=Incorrect Position, G=Correct Position)")

    input_results.append(input_result_states)

if len(input_results) == 0:
    raise ValueError("No inputs")

game = Game()
paths = {}

# start going through the potential solutions and seeing if the input could work
for solution in game.VALID_SOLUTIONS:
    print(f"Solution {solution}")
    could_be = [[] for i in range(len(input_results))]

    for guess in game.VALID_GUESSES:
        check_guess = Game.check_guess(guess, solution)
        for i, input_result in enumerate(input_results):
            if input_result == check_guess:
                could_be[i].append(guess)

    # if every input slot has candidate words, this is good
    if all(could_be):
        paths[solution] = could_be

for solution, path in paths.items():
    print(f"Solution could be {solution}")
    for i, guesses in enumerate(path):
        guesses_str = ' '.join(sorted(guesses))
        print(f"  Guess {i} matching {sys.argv[1+i]} could be: {guesses_str}")
