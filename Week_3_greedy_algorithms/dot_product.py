# Maximum Advertisement Revenue (Maximum Dot Product) Problem

# Goal: Design an algorithm that given inputs of a list of prices, a list of clicks, and the length of the list 'n',
#       returns the maximum dot product (price * clicks) from the possible arrangements of clicks and prices.

# from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    # Optimized greedy way - use Python's sort function at start, then a simple multiplication loop
    max_dot = 0
    first_sequence.sort(reverse=True)
    second_sequence.sort(reverse=True)
    for i in range(len(first_sequence)):
        max_dot += first_sequence[i] * second_sequence[i]
    return max_dot

    # # Unoptimized greedy way - better than naive, but still slow - O(n^2)
    # max_dot = 0
    # for i in range(len(first_sequence)):
    #     max_i = first_sequence.index(max(first_sequence))
    #     max_j = second_sequence.index(max(second_sequence))
    #     max_dot += first_sequence[max_i] * second_sequence[max_j]
    #     first_sequence.pop(max_i)
    #     second_sequence.pop(max_j)
    # return max_dot

    # # Slow, naive way - looks at every single possible arrangement of list 2 * list 1
    # max_product = 0
    # for permutation in permutations(second_sequence):
    #     dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
    #     max_product = max(max_product, dot_product)
    # return max_product


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
