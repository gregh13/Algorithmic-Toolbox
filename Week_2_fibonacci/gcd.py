# Greatest Common Divisor Problem

# Goal: Design an algorithm that given an input of two numbers 'a' and 'b', returns their greatest common denominator
#       *** Must not only be accurate, but fast. Even for very large inputs of 'n' (e.g. 100 trillion)

import math


def gcd(a, b):
    # Their way (brilliant!)
    # if b == 0:
    #     return a
    # a_prime = a % b
    # return gcd(b, a_prime)

    # My way (much faster than naive, but still too slow for very large numbers (n > 10^15)
    sm = min(a, b)
    lg = max(a, b)
    gcd_list = []
    lim = math.floor(math.sqrt(sm))
    for d in range(1, (lim + 1)):
        if sm % d == 0:
            if lg % (sm / d) == 0:
                return int((sm / d))
            gcd_list.append(d)
    gcd_list.reverse()
    for num in gcd_list:
        if lg % num == 0:
            return num
    return 1

    # Slow, brute force way
    # current_gcd = 1
    # for d in range(2, min(a, b) + 1):
    #     if a % d == 0 and b % d == 0:
    #         if d > current_gcd:
    #             current_gcd = d
    #
    # return current_gcd


if __name__ == "__main__":
    a, b = map(int, input().split())
    # t0 = time.process_time()
    print(gcd(a, b))
    # t1 = time.process_time()
    # print(f"Time elasped: {t1 - t0}")
