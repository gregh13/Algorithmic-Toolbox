
# Goal: Design an algorithm that given an input of two numbers 'a' and 'b', returns their least common multiple
#       *** Must not only be accurate, but fast. Even for very large inputs of 'n' (e.g. 100 trillion)

def lcm(a, b):
    # My way (building off their gcd way)
    def gcd(a, b):
        if b == 0:
            return a
        a_prime = a % b
        return gcd(b, a_prime)
    gcd = gcd(a, b)
    return int((a * b) / gcd)

    # Slow, naive way
    # for l in range(1, a * b + 1):
    #     if l % a == 0 and l % b == 0:
    #         return l
    #
    # assert False


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

