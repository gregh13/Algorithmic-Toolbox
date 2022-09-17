import random
import sys

n = int(sys.argv[1])
n_range = int(sys.argv[2])
myseed = int(sys.argv[3])

random.seed(myseed)
print(n)
# print(n_range)
# print(f"Seed number: {myseed}")

print(' '.join([str(random.randint(0, n_range)) for i in range(n)]))
