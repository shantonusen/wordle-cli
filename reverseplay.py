#!/usr/bin/env python3

# Determine a solution and guesses based on set of result rows

import os
import sys
from collections import Counter
import itertools
import multiprocessing

from wordle import Game, LetterStates

def parse_args():
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

    return input_results

def f_solve_for_solution(args):
    (game, result_state, solution, j, jlen) = args

    possible_guesses = set()
    print(f"  Solving for solution {solution} ({j} out of {jlen})")
    for guess in game.VALID_GUESSES:
        check_guess = Game.check_guess(guess, solution)
        if result_state == check_guess:
            possible_guesses.add(guess)

    return (solution, possible_guesses)

if __name__ == '__main__':
    input_results = parse_args()
    game = Game()

    multiprocessing.set_start_method('spawn')

    solutions = {}
    # for each solution, maintain an array of sets of what guess could have been used for each round.
    for solution in game.VALID_SOLUTIONS:
        solutions[solution] = [None for input_result in input_results]

    # for each round, try to figure out what guesses would work for each solution
    for i, result_state in enumerate(input_results):
        print(f"Solving for row {i} {sys.argv[1+i]}")
        solutions_to_prune = set()
        j = 0
        jlen = len(solutions)
        for solution, row_arrays in solutions.items():
            (solution, possible_guesses) = f_solve_for_solution((game, result_state, solution, j, jlen))
            if len(possible_guesses):
                solutions[solution][i] = possible_guesses
            else:
                solutions_to_prune.add(solution)
            j += 1
        for solution in solutions_to_prune:
            print(f"    No valid guesses for solution {solution} for row {i}, pruning...")
            del solutions[solution]

    common_words = set(game.VALID_SOLUTIONS)
    for solution, row_arrays in solutions.items():
        likely_guesses = []
        unlikely_guesses = []
        for i, guesses in enumerate(row_arrays):
    #        guesses_str = ' '.join(sorted(guesses))
    #        print(f"  Guess {i} matching {sys.argv[1+i]} could be: {guesses_str}")
            likely_guesses.append(guesses & common_words)
            unlikely_guesses.append(guesses - common_words)

        print(f"Solution could be {solution}")

        for i, guesses in enumerate(row_arrays):
            guesses_str = ' '.join(sorted(likely_guesses[i]))
            guesses_str += ' (could also be ' + ' '.join(sorted(unlikely_guesses[i])) + ')'
            print(f"  Guess {i} matching {sys.argv[1+i]} could be: {guesses_str}")
