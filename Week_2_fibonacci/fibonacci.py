
# Goal: Design an algorithm that given an input 'n', returns the 'nth' term in the Fibonacci sequence.
#       *** Must not only be accurate, but fast. Even for very large inputs of 'n' (e.g. 100,000+)

import time


# Testing various methods and their run times
def fibonacci_number1(n):
    # My way - works fine except is too slow for very large values of n
    fib = [0, 1]
    for i in range(n-1):
        new = fib[-2] + fib[-1]
        fib.append(new)
    return fib[n]


def fibonacci_number2(n):
    # Similar to above, but doesn't save value in a variable and uses i and i+1 instead of -2 and -1 for list indexing
    fib = [0, 1]
    for i in range(n+1):
        fib.append(fib[i+1] + fib[i])
    return fib[n]


def fibonacci_number3(n):
    # Creating a fixed size array from the start - very fast, but problems with memory for large inputs of n
    f = [None] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


def fibonacci_number4(n):
    # Avoid setting value equal to by using modulo pointer arithmetic - very slow!
    f = [0, 1, 1]
    for i in range(2, n+1):
        f[i % 3] = f[(i-1) % 3] + f[(i-2) % 3]
    return f[n % 3]


def fibonacci_number5(n):
    # Slow, brute force way
    new = 0
    first = 1
    second = 0
    for i in range(n-1):
        new = (first + second)
        second = first
        first = new
    return new


if __name__ == '__main__':
    input_n = int(input())
    t0 = time.perf_counter()
    fibonacci_number1(input_n)
    t1 = time.perf_counter()
    print(f"Time elapsed for #1: {t1 - t0}")
    time.sleep(1)
    t2 = time.perf_counter()
    fibonacci_number2(input_n)
    t3 = time.perf_counter()
    print(f"Time elapsed for #2: {t3 - t2}")
    time.sleep(1)
    t4 = time.perf_counter()
    fibonacci_number3(input_n)
    t5 = time.perf_counter()
    print(f"Time elapsed for #3: {t5 - t4}")
    time.sleep(1)
    t6 = time.perf_counter()
    fibonacci_number4(input_n)
    t7 = time.perf_counter()
    print(f"Time elapsed for #4: {t7 - t6}")
    time.sleep(1)
    t8 = time.perf_counter()
    fibonacci_number5(input_n)
    t9 = time.perf_counter()
    print(f"Time elapsed for #5: {t9 - t8}")
    # print("Trial: ", )
    # print("Check: ", )
