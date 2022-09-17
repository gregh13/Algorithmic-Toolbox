
# Goal: Design an algorithm that given an input of a range of two numbers, returns the last digit of the sum of terms
#       in the Fibonacci sequence that occurs between the 'from' and the 'to' term. Ex: 5 8 --> sum of 5th to 8th term
#       *** Must not only be accurate, but fast. Even for incredibly large input ranges of 'n' (e.g. 10 ^ 100)


def fibonacci_partial_sum_naive(from_, to):

    def normal_sum(n):
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
        return _sum

    if to <= 1:
        return to

    sum_to = normal_sum(to)
    sum_from = normal_sum(from_ - 1)
    if from_ < 1:
        sum_answer = sum_to
    else:
        sum_answer = sum_to - sum_from
    return sum_answer % 10


    # Slow, naive way
    # _sum = 0
    #
    # current = 0
    # _next  = 1
    #
    # for i in range(to + 1):
    #     if i >= from_:
    #         _sum += current
    #
    #     current, _next = _next, current + _next
    #
    # return _sum % 10


# Used to stress testing the above function
def fibonacci2(from_, to):
    # My way - works fine except is too slow for very large values of n
    if to <= 1:
        return to
    fib = [0, 1]
    _sum = 0
    for i in range(to+1):
        fib.append((fib[i+1] + fib[i]) % 10)
        if i >= from_:
            _sum += fib[i]
    return _sum % 10


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive(from_, to))
    # print("Trial: ", fibonacci_partial_sum_naive(from_, to))
    # print("Check: ", fibonacci2(from_, to))

