import random
import sys
import os
import time

# accept the number of tests as a command line parameter
tests = int(sys.argv[1])
# accept the parameter for the tests as a command line parameter
n = int(sys.argv[2])
# accept the parameter for the tests as a command line parameter
n_range = int(sys.argv[3])

for i in range(tests):
    print("Test # " + str(i))
    # run the generator gen.py with parameter n, n_range, and the seed i
    os.system("python3 gen.py " + str(n) + " " + str(n_range) + " " + str(i) + " > input.txt")
    # run the model solution model.py
    # Notice that it is not necessary that solution is implemented in
    # python , you can as well run ./model <input.txt >model.txt for a C++
    # solution.
    t1 = time.perf_counter()
    os.system("python3 largest_number_model.py <input.txt >model.txt ")
    # run the main solution
    t2 = time.perf_counter()
    os.system("python3 largest_number_naive.py <input.txt >main.txt ")
    t3 = time.perf_counter()
    print(f"Model Time: {t2-t1}")
    print(f"Model Time: {t3 - t2}")
    # read the output of the model solution:
    with open('model.txt') as f:
        model = f.read()
    print("Model: ", model)
    # read the output of the main solution:
    with open('main.txt') as f:
        main = f.read()
    print("Main : ", main)
    if model != main:
        break
