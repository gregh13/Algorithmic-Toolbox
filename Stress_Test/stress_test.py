import random
import sys
import os

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
    os.system("python3 model.py <input.txt >model.txt ")
    # run the main solution
    os.system("python3 main.py <input.txt >main.txt ")
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

