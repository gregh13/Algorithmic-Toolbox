# Generic stress test template

import random
import sys
import os

# accept the number of tests as a command line parameter
tests = int(sys.argv[1])

# Number of Segments
n = sys.argv[2]
# Segment value range ceiling
n_range = sys.argv[3]

# Number of Points
m = sys.argv[4]
# Point value range ceiling
m_range = sys.argv[5]


for i in range(tests):
    print("Test # " + str(i))
    # Writes number of segments and points into input.txt
    os.system("python3 pre_gen.py " + n + " " + m + " > input.txt")

    # Randomly generates segments and writes them into input.txt
    os.system("python3 segments_gen.py " + n + " " + n_range + " " + str(i) + " >> input.txt")

    # Randomly generates points and writes them into input.txt
    os.system("python3 points_gen.py " + m + " " + m_range + " " + str(i) + " >> input.txt")

    temp = open("input.txt", 'r').read().splitlines()
    all_inputs = ' '.join(temp)
    # print(all_inputs)
    with open('input.txt', 'w') as f:
        f.write(all_inputs)

    # Run the naive, but correct model
    os.system("python3 points_and_segments_naive_way.py <input.txt >naive.txt ")

    print("Naive finished")
    # Run test model with inputs
    os.system("python3 points_and_segments.py <input.txt >model.txt ")
    print("Model finished")

    # Read the output of the model solution:
    with open('model.txt') as f:
        model = f.read()
    print("Model: ", model)
    # Read the output of the naive solution:
    with open('naive.txt') as f:
        naive = f.read()
    print("Naive: ", naive)
    if model != naive:
        print("\nBROKEN\n")
        break

