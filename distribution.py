#!/usr/bin/env python3

import os
from collections import Counter
import itertools

path_solutions="data/solutions.txt"
with open(os.path.join(os.path.dirname(__file__), path_solutions), "r") as f:
    valid_solutions = itertools.chain.from_iterable(l.upper() for l in f.read().splitlines())

counter = Counter(valid_solutions)
distribution = counter.most_common()
total = sum(counter.values())

print("LETTER COUNT PERCENT")
for (letter, count) in distribution:
    print("{:<6s} {:>5d} {:>6.1f}%".format(letter, count, count/total*100.0))
