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

solutions = {}
# for each solution, maintain an array of sets of what guess could have been used for each round.
for solution in game.VALID_SOLUTIONS:
    solutions[solution] = [set() for input_result in input_results]

# for each round, try to figure out what guesses would work for each solution
for i, result_state in enumerate(input_results):
    print(f"Solving for row {i} {sys.argv[1+i]}")
    solutions_to_prune = set()
    j = 0
    jlen = len(solutions)
    for solution, row_arrays in solutions.items():
        print(f"  Solving for solution {solution} ({j} out of {jlen})")
        for guess in game.VALID_GUESSES:
            check_guess = Game.check_guess(guess, solution)
            if result_state == check_guess:
#                print(f"could be {result_state} == {check_guess} for {guess}")
                row_arrays[i].add(guess)
        if len(row_arrays[i]) == 0:
            solutions_to_prune.add(solution)
        j += 1
    for solution in solutions_to_prune:
        print(f"    No valid guesses for solution {solution} for row {i}, pruning...")
        del solutions[solution]

common_words = set(game.VALID_SOLUTIONS)
for solution, row_arrays in solutions.items():
    print(f"Solution could be {solution}")
    likely_guesses = []
    unlikely_guesses = []
    for i, guesses in enumerate(row_arrays):
#        guesses_str = ' '.join(sorted(guesses))
#        print(f"  Guess {i} matching {sys.argv[1+i]} could be: {guesses_str}")
        likely_guesses.append(guesses & common_words)
        unlikely_guesses.append(guesses - common_words)

    for i, guesses in enumerate(row_arrays):
        guesses_str = ' '.join(sorted(likely_guesses[i]))
        guesses_str += ' (could also be ' + ' '.join(sorted(unlikely_guesses[i])) + ')'
        print(f"  Guess {i} matching {sys.argv[1+i]} could be: {guesses_str}")
