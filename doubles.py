#!/usr/bin/env python3

import os
from collections import Counter
import itertools

path_solutions="data/solutions.txt"
# path_solutions="data/guesses.txt"
with open(os.path.join(os.path.dirname(__file__), path_solutions), "r") as f:
    valid_solutions = [l.upper() for l in f.read().splitlines()]


words_with_triple_and_double = set()
words_with_triple_letters = set()
words_with_two_doubles = set()
words_with_one_double = set()

for solution in valid_solutions:
    counter = Counter(solution)
    distribution = counter.most_common()
    if distribution[0][1] >= 4:
        assert(False and "Really???")
    elif distribution[0][1] == 3 and distribution[1][1] == 2:
        words_with_triple_and_double.add(solution)
    elif distribution[0][1] == 3:
        words_with_triple_letters.add(solution)
    elif distribution[0][1] == 2 and distribution[1][1] == 2:
        words_with_two_doubles.add(solution)
    elif distribution[0][1] == 2:
        words_with_one_double.add(solution)

print("Answers with a triple repeating letters, and a double repeating letter: {}/{}".format(len(words_with_triple_and_double), len(valid_solutions)))
for solution in sorted(words_with_triple_and_double):
    print("  {}".format(solution))

print("Answers with triple repeating letters: {}/{}".format(len(words_with_triple_letters), len(valid_solutions)))
for solution in sorted(words_with_triple_letters):
    print("  {}".format(solution))

print("Answers with double-double repeating letters: {}/{}".format(len(words_with_two_doubles), len(valid_solutions)))
for solution in sorted(words_with_two_doubles):
    print("  {}".format(solution))

print("Answers with double repeating letters: {}/{}".format(len(words_with_one_double), len(valid_solutions)))
print("  <not printed>")
#for solution in sorted(words_with_one_double):
#    print("  {}".format(solution))
