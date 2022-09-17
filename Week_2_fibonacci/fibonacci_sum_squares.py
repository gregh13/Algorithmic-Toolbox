# Fibonacci Sum of Squares Problem (Last Digit)

# Goal: Design an algorithm that given an input 'n', returns the last digit of the sum of squared terms in the Fibonacci
#       sequence up to the 'nth' term. Ex: 5 --> 0+1+1+4+9+25 = 40 --> last digit = 0
#       *** Must not only be accurate, but fast. Even for incredibly large inputs of 'n' (e.g. 10 ^ 100)


def fibonacci_sum_squares(n):
    if n <= 1:
        return n
    fib = [0, 1]
    _sum = 0
    # Using Pisano Fibonacci Theory, the last digit in the series repeats every 60 numbers (period of modulo 10)
    period = 60
    modulo = 10
    loop_length = min(n, period)
    for i in range(loop_length + 1):
        fib.append((fib[i+1] + fib[i]) % modulo)
        _sum += (fib[i] ** 2) % modulo
    if n > period:
        num_periods = n // period
        remainder = n % period
        _sum = (_sum * num_periods) % modulo
        for j in range(remainder + 1):
            _sum += (fib[j] ** 2) % modulo
    return _sum % modulo


    # This is faster than appending, but runs into memory issues with very large inputs of n
    # if n <= 1:
    #     return n
    # f = [0] * (n+1)
    # f[0] = 0
    # f[1] = 1
    # _sum = 1
    # for i in range(2, n+1):
    #     f[i] = (f[i-1] + f[i-2]) % 10
    #     _sum += f[i] ** 2
    # return _sum % 10


    # Slow, naive way
    # if n <= 1:
    #     return n
    #
    # previous, current, sum = 0, 1, 1
    #
    # for _ in range(n - 1):
    #     previous, current = current, previous + current
    #     sum += current * current
    #
    # return sum % 10


# Used to stress testing the above function
def fibonacci2(n):
    # My way - works fine except is too slow for very large values of n
    if n <= 1:
        return n
    fib = [0, 1]
    _sum = 0
    for i in range(n+1):
        fib.append((fib[i+1] + fib[i]) % 10)
        _sum += fib[i] ** 2
    return _sum % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
    # print("Trial: ", fibonacci_sum_squares(n))
    # print("Check: ", fibonacci2(n))
