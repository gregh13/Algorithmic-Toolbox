
# Goal: Design an algorithm that given an input 'n' and a modulo 'm', returns the 'nth' term % m in the Fibonacci series
#       *** Must not only be accurate, but fast. Even for incredibly large inputs of 'n' (e.g. 10 ^ 30) as well as
#           for large inputs of 'm' (1 < m < 50,000). The proportion of 'n' to 'm' will affect the speed of results.
#           A very large 'n' and a large 'm' could slow things down.

def fibonacci_huge_naive(n, m):
    if m <= 0:
        return "Modulo must be greater than 0!"
    if m == 1:
        # anything divided by 1 will have no remainders
        return 0
    if m > 50000:
        return "Please choose a smaller value for m (modulo)"
    if n <= 1:
        return n
    fib = [0, 1]
    found = False
    i = 0
    while not found:
        fib.append((fib[i+1] + fib[i]) % m)
        fl = len(fib)
        if fl % 2 == 0:
            mid = int(fl / 2)
            if fib[:mid] == fib[mid:]:
                period = mid
                found = True
        i += 1
    #print(f"Period of modulo({m}): {period}")
    remainder = n % period
    #print(f"{n} % {period} = {remainder} ")
    return fib[remainder]

    # Slow, naive way
    # if n <= 1:
    #     return n
    #
    # previous = 0
    # current = 1
    #
    # for _ in range(n - 1):
    #     previous, current = current, previous + current
    #
    # return current % m


# Used to stress testing the above function
def fibonacci2(n, m):
    # My way - works fine except is too slow for very large values of n
    if n <= 1:
        return n
    fib = [0, 1]
    for i in range(n+1):
        fib.append((fib[i+1] + fib[i]) % m)
    return fib[n]


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
    # print("Trial: ", fibonacci_huge_naive(n, m))
    # print("Check: ", fibonacci2(n, m))
