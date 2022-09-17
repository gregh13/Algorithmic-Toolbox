# Fibonacci Last Digit of Sum Problem

# Goal: Design an algorithm that given an input 'n', returns the last digit of the sum of terms in the Fibonacci
#       sequence up to the 'nth' term. Ex: 5 --> 0+1+1+2+3+5 = 12 --> last digit = 2
#       *** Must not only be accurate, but fast. Even for incredibly large inputs of 'n' (e.g. 10 ^ 100)

def fibonacci_sum(n):
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
        _sum += fib[i]
    if n > period:
        num_periods = n // period
        remainder = n % period
        _sum = (_sum * num_periods) % modulo
        for j in range(remainder + 1):
            _sum += fib[j] % modulo
    return _sum % modulo


    # My way - works on everything, but takes too long for really large values of n
    # if n <= 1:
    #     return n
    # fib = [0, 1]
    # _sum = 0
    # for i in range(n+1):
    #     fib.append((fib[i+1] + fib[i]) % 10)
    #     _sum += fib[i]
    # return _sum % 10


    # Slow, naive way
    # if n <= 1:
    #     return n
    #
    # previous, current, _sum = 0, 1, 1
    #
    # for _ in range(n - 1):
    #     previous, current = current, previous + current
    #     _sum += current
    #
    # return _sum % 10


# Used to stress testing the above function
def fibonacci2(n):
    # My way - works fine except is too slow for very large values of n
    if n <= 1:
        return n
    fib = [0, 1]
    _sum = 0
    for i in range(n+1):
        fib.append((fib[i+1] + fib[i]) % 10)
        _sum += fib[i]
    return _sum % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
    # print("Trial: ", fibonacci_sum(n))
    # print("Check: ", fibonacci2(n))

