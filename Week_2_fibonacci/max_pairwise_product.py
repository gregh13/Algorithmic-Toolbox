# Max Pairwise Product Problem

# Goal: Design a simple algorithm that returns the greatest possible product of any two numbers in an array

def max_pairwise_product(numbers):
    # My way
    first = max(numbers)
    index = numbers.index(first)
    numbers.pop(index)
    second = max(numbers)
    return first * second

    # Slow, brute force way
    # n = len(numbers)
    # max_product = 0
    # for first in range(n):
    #     for second in range(first + 1, n):
    #         max_product = max(max_product,
    #             numbers[first] * numbers[second])
    # return max_product


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
