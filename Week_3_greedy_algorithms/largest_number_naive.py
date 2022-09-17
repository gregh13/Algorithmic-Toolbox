# Largest Number with Concatenation Problem

# Goal: Design an algorithm that given an input of a list of numbers (as strings), returns the largest possible number
#       via concatentating all of the numbers in the list together.
#       Ex: [3, 7, 9, 10, 2, 24, 4, 1] --> 9743242110


from itertools import permutations

# def largest_number_greedy(numbers):
#     Divide and conquer way - divide by leading digit, sort small list, then add to master list
#     turn numbers into string in event they are integers
#     numbers = list(map(str, numbers))
#     numbers.sort()
#     largest = ""
#     for i in range(9, 0, -1):
#         # print("i: ", i)
#         single_digits = []
#         non_single_digits = []
#         for num in numbers:
#             if num[0] == str(i):
#                 # print(f"Number: {num}\nLength of number: {len(num)}")
#                 if len(num) > 1:
#                     non_single_digits.append(num)
#                 else:
#                     single_digits.append(num)
#                 # make list shorter for faster searches throughout the loop
#                 # numbers.pop(numbers.index(num))
#         non_single_digits.sort(reverse=True)
#         # print(non_single_digits)
#         add_later = []
#         for non_single in non_single_digits:
#             added = False
#             for d in non_single:
#                 if str(i) < d:
#                     largest += non_single
#                     added = True
#                     break
#             if not added:
#                 add_later.append(non_single)
#         for single in single_digits:
#             largest += single
#         for n in add_later:
#             largest += n
#     # Check for zeros
#     for number in numbers:
#         if number == "0":
#             largest += number
#     return largest




# def largest_number_naive(numbers):
#     # Slow, naive way - iterates over all possible arrangements of the list
#     numbers = list(map(str, numbers))
#     largest = 0
#     for permutation in permutations(numbers):
#         largest = max(largest, int("".join(permutation)))
#     return largest


def largest_number_naive(numbers):
    # Slow, naive way - iterates over all possible arrangements of the list
    numbers = list(map(str, numbers))
    largest = ""
    while numbers:
        sub_largest = "0"
        for number in numbers:
            comparison = [number, str(sub_largest)]
            best_perm = ('0', '0')
            for permutation in permutations(comparison):
                before = int(sub_largest)
                # print(permutation)
                sub_largest = max(int(sub_largest), int("".join(permutation)))
                if sub_largest != before:
                    best_perm = permutation
            sub_largest = best_perm[0]
        best_num = best_perm[0]
        largest += best_num
        numbers.pop(numbers.index(best_num))
    return largest


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
    # print(largest_number_greedy(input_numbers))
