# Generic stress test random number template

import random
import sys

n = int(sys.argv[1])
n_range = int(sys.argv[2])
myseed = int(sys.argv[3])

random.seed(myseed)
# print(f"Number of inputs each test: {n}")
# print(f"Range of inputs: 0 to {n_range}")
# print(f"Seed number: {myseed}")

print(' '.join([str(random.randint(-100_000_000, n_range)) for i in range(n)]))
