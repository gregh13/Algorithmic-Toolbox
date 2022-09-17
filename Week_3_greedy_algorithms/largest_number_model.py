# Largest Number with Concatenation Problem

# Goal: Design an algorithm that given an input of a list of numbers (as strings), returns the largest possible number
#       via concatentating all of the numbers in the list together.
#       Ex: [3, 7, 9, 10, 2, 24, 4, 1] --> 9743242110


from itertools import permutations


def largest_number_greedy_complex(numbers):
    def check_value(term, number, largest):
        same = False
        if number[term] > largest[term]:
            return int(number), same
        elif number[term] == largest[term]:
            same = True
            return int(largest), same
        else:
            return int(largest), same

    largest = ""
    while numbers:
        largest_val = 0
        for number in numbers:
            # Get minimum length of digits between number and current largest
            min_val = str(min(largest_val, int(number)))
            max_val = str(max(largest_val, int(number)))
            min_length = len(min_val)
            max_length = len(max_val)
            same = False
            for i in range(min_length):
                largest_val, same = check_value(i, number, str(largest_val))
                if not same:
                    break
            # Now to catch comparison like 365 and 3654
            check_digit = 0
            # Check for repeat numbers in list
            if same and max_length != min_length:
                checking = True
                diff = max_length - min_length
                while checking:
                    for j in range(diff):
                        # Check any trailing digits
                        max_digit = max_val[j + min_length]
                        min_digit = min_val[check_digit]
                        if max_digit < min_digit:
                            # trailing number is smaller, so min_val goes first --> 36 and 361, 36 should be first
                            largest_val = int(min_val)
                            checking = False
                            break
                        elif max_digit > min_digit:
                            # trailing is larger, so max_val goes first --> 74 and 7481, 7481 should be first
                            largest_val = int(max_val)
                            checking = False
                            break
                        elif max_digit == min_digit:
                            if j == diff - 1:
                                check_digit += 1
                            # need to move to compare the next digit in the min_val --> 243 and 2432
                            if check_digit >= min_length:
                                checking = False
                                break
        largest += str(largest_val)
        # Remove largest number
        numbers.remove(str(largest_val))

    # Check if list was all zeros
    if int(largest) < 1:
        largest = "0"
    return largest

    #
    #
    # Old Way, Failed Attempt
    # Divide and conquer way - divide by leading digit, sort small list, then add to master list
    # turn numbers into string in event they are integers
    # numbers = list(map(str, numbers))
    # numbers.sort()
    # largest = ""
    # for i in range(9, 0, -1):
    #     # print("i: ", i)
    #     single_digits = []
    #     non_single_digits = []
    #     for num in numbers:
    #         if num[0] == str(i):
    #             # print(f"Number: {num}\nLength of number: {len(num)}")
    #             if len(num) > 1:
    #                 non_single_digits.append(num)
    #             else:
    #                 single_digits.append(num)
    #             # make list shorter for faster searches throughout the loop
    #             # numbers.pop(numbers.index(num))
    #     print("Non_single before sort: ", non_single_digits)
    #     non_single_digits.sort(reverse=True)
    #     print("Non_single after sort: ", non_single_digits)
    #     add_later = []
    #     for non_single in non_single_digits:
    #         added = False
    #         for d in non_single:
    #             if str(i) < d:
    #                 print("Added first: ", non_single)
    #                 largest += non_single
    #                 added = True
    #                 break
    #             elif str(i) > d:
    #                 add_later.append(non_single)
    #                 added = True
    #                 break
    #         # This means number is a repeat of single digit (i.e. 4 and 44 and 444), same placement as single digits
    #         if not added:
    #             single_digits.append(non_single)
    #     for single in single_digits:
    #         largest += single
    #     print("Add_later List: ", add_later)
    #     for n in add_later:
    #         largest += n
    # # Check for zeros
    # for number in numbers:
    #     if number == "0":
    #         largest += number
    # return largest


def largest_number_greedy_simple(numbers):
    # Greedy way - only compare permutations of two numbers, take the 'bigger' of the two and repeat.
    numbers = list(map(str, numbers))
    largest = ""
    while numbers:
        sub_largest = "0"
        best_perm = (0, 0)
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
        numbers.remove(best_num)
    return largest


# def largest_number_naive(numbers):
#     # Slow, naive way - iterates over all possible arrangements of the list
#     numbers = list(map(str, numbers))
#     largest = 0
#     for permutation in permutations(numbers):
#         largest = max(largest, int("".join(permutation)))
#     return largest


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    # print(largest_number_naive(input_numbers))
    # print(largest_number_greedy_simple(input_numbers))
    print(largest_number_greedy_complex(input_numbers))

