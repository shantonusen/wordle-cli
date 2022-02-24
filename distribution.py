#!/usr/bin/env python3

import os
from collections import Counter
import itertools

path_solutions="data/solutions.txt"
with open(os.path.join(os.path.dirname(__file__), path_solutions), "r") as f:
    valid_solutions = [l.upper() for l in f.read().splitlines()]
    all_letters_in_all_words = itertools.chain.from_iterable(valid_solutions)
    unique_letters_in_all_words = itertools.chain.from_iterable(map(set, valid_solutions))

counter = Counter(all_letters_in_all_words)
counter_unique_letters = Counter(unique_letters_in_all_words)
distribution = counter.most_common()
total = sum(counter.values())
total_unique_words = len(valid_solutions)

print("LETTER COUNT PERCENT  OCCURSIN PERCWORDS")
for (letter, count) in distribution:
    print("{:<6s} {:>5d} {:>6.1f}% {:>9s} {:>8.1f}%".format(letter,
                                                            count,
                                                            count/total*100.0,
                                                            str(counter_unique_letters[letter])+"/"+str(total_unique_words),
                                                            counter_unique_letters[letter]/total_unique_words*100.0))
