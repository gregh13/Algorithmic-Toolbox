
# Goal: Design an algorithm that given an input 'n', returns the last digit of the 'nth' term in the Fibonacci sequence.
#       *** Must not only be accurate, but fast. Even for very large inputs of 'n' (e.g. 1 million+)

def fibonacci_last_digit(n):
    # My way
    f = [None] * (n+1)
    if not f:
        print("Array not created")
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = (f[i-1] + f[i-2]) % 10
    return f[n]

    # Slow, Naive Way
    # if n <= 1:
    #     return n
    #
    # previous = 0
    # current = 1
    #
    # for _ in range(n - 1):
    #     previous, current = current, previous + current
    #
    # return current % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
