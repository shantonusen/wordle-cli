#!/usr/bin/env python3

import os
from collections import Counter
import itertools

path_solutions="data/solutions.txt"
# path_solutions="data/guesses.txt"
with open(os.path.join(os.path.dirname(__file__), path_solutions), "r") as f:
    valid_solutions = [l.upper() for l in f.read().splitlines()]


solutions_minus_letter_at_this_index = [dict() for i in range(5)]
solutions_minus_letter_at_this_index_counter = Counter()

for solution in valid_solutions:
    for i in range(0, 5):
        solution_minus_index = solution[:i] + solution[i+1:]
        if solution_minus_index not in solutions_minus_letter_at_this_index[i]:
            solutions_minus_letter_at_this_index[i][solution_minus_index] = set()
        solutions_minus_letter_at_this_index[i][solution_minus_index].add(solution)
        solutions_minus_letter_at_this_index_counter[(solution_minus_index, i)] += 1

most_off_by_ones = [x for x in solutions_minus_letter_at_this_index_counter.most_common() if x[1] >= 4]
for ((off_by_one, position), count) in most_off_by_ones:
    other_solutions = solutions_minus_letter_at_this_index[position][off_by_one]
    pattern = off_by_one[:position] + "X" + off_by_one[position:]
    print(f"{pattern} has {count} potential solutions:")
    for other_solution in sorted(other_solutions):
        print(f"  {other_solution}")
