# Inversion Count Problem

# Goal: Design an algorithm that when given a sequence of numbers as an input, determine the number of 'inversions' that
#       occur in the list. An 'inversion' is when a lower number comes after a higher number.
#       Example: 9 1 6 2 --> 4 inversions     and      2 1 6 5 3 6 22 0 11 5 --> 16 inversions


from itertools import combinations


def inversion_count_mergesort(original_sequence):
    def merge(left_seq, right_seq):
        merged_seq = []
        left_length = len(left_seq)
        while left_seq and right_seq:
            left = left_seq[0]
            right = right_seq[0]
            if left <= right:
                merged_seq.append(left_seq.pop(0))
                left_length -= 1
            else:
                merged_seq.append(right_seq.pop(0))

                # Multiply by list length as that's how many 'places' it must be moved (i.e. inversions)
                inversions[0] += 1 * left_length

        # One list will be exhausted above, must add remaining items left in other list
        if left_seq:
            for val in left_seq:
                merged_seq.append(val)
        else:
            for val in right_seq:
                merged_seq.append(val)

        return merged_seq

    def merge_sort(sequence):

        n = len(sequence)
        if n == 1:
            return sequence

        mid = n // 2
        left_sequence = merge_sort(sequence[:mid])
        right_sequence = merge_sort(sequence[mid:])
        new_seq = merge(left_sequence, right_sequence)
        return new_seq

    inversions = [0]
    merge_sort(original_sequence)
    return inversions[0]


def inversions_recursive_divide(sequence):
    # A variation of the quicksort 3, performs well, but not as well as the above merge sort
    # Main issue is that since the original order of the sequence determines the inversion numbers,
    # the shuffling around of sorted numbers doesn't work, and with my variation of creating two new lists
    # the random starting pivot element is taken away, meaning that the first element is always the pivot
    # This is especially slow for nearly sorted inputs as the division sizes will be unbalanced
    def divide_and_conquer(sequence):
        len_seq = len(sequence)
        if len_seq < 2:
            return
        lower_list = []
        higher_list = []
        pivot = sequence[0]
        midpoint_1 = 0
        midpoint_2 = 1
        for i in range(1, len_seq):
            val = sequence[i]
            if val < pivot:
                lower_list.append(val)
                inversions[0] += i - midpoint_1
                midpoint_1 += 1
                midpoint_2 += 1
            elif val > pivot:
                higher_list.append(val)
            else:
                inversions[0] += i - midpoint_2
                midpoint_2 += 1

        if len(lower_list) < len(higher_list):
            divide_and_conquer(lower_list)
            divide_and_conquer(higher_list)
        else:
            divide_and_conquer(higher_list)
            divide_and_conquer(lower_list)

    inversions = [0]
    divide_and_conquer(sequence)
    return inversions[0]


# def inversions_second_best(sequence):
#     def calc_indices(elements):
#         # Single pass to find all index values of the both the max and min value in a list
#         if not elements:
#             return 0, [], 0, []
#         max_indices = [0]
#         min_indices = [0]
#         max_val = elements[0]
#         min_val = elements[0]
#         for i, value in enumerate(elements[1:]):
#             # print("Value: ", value)
#             # print("Min List: ", min_indices)
#             # print("Max List: ", max_indices)
#             if value < max_val:
#                 if value < min_val:
#                     min_val = value
#                     min_indices = [i+1]
#                     continue
#                 elif value == min_val:
#                     min_indices.append(i+1)
#                     continue
#                 else:
#                     continue
#             elif value == max_val:
#                 max_indices.append(i+1)
#             else:
#                 max_val = value
#                 max_indices = [i+1]
#         return max_val, max_indices, min_val, min_indices
#
#     inversions = 0
#
#     while True:
#         # print("Sequence: ", sequence)
#         # Calculate the current max value and all the indices where the max is located
#         max_val, max_index_list, min_val, min_index_list = calc_indices(sequence)
#
#         # Used to calculate the number of inversion
#         seq_length = len(sequence)
#         max_index_length = len(max_index_list)
#         min_index_used = 0
#
#         # End check to exit while loop when all maxes have been accounted for
#         if seq_length <= max_index_length:
#             return inversions
#
#         for max_index_val in max_index_list:
#             # print("MAX LOOOP")
#             # Subtract duplicates from sequence length, the get the range from max index to end of sequence
#             inversions += ((seq_length - max_index_length) - max_index_val)
#
#             # print("inversions: ", inversions)
#             # Prepare for next iteration
#             max_index_length -= 1
#
#         # print(min_index_list)
#         for min_index_val in min_index_list:
#             # print("\nMIN LOOOP")
#
#             # Subtract duplicates from sequence length, the get the range from min index to end of sequence
#             inversions += (min_index_val - min_index_used)
#
#             # print("inversions pre_correction: ", inversions)
#             # Prepare for next iteration
#             min_index_used += 1
#
#             # Calculate duplicate counts from above max_index iteration
#             correction_val = 0
#             for max_i in max_index_list:
#                 if max_i < min_index_val:
#                     correction_val += 1
#
#             # Correct inversion count
#             inversions -= correction_val
#
#         # Combine index lists to prepare for removal
#         all_indices = max_index_list + min_index_list
#         all_indices.sort(reverse=True)
#
#         # Del in reverse order so that the previous indices don't get affected
#         for index in all_indices:
#             # Remove the current max value from the original sequence, preparing for next iteration with smaller list
#             del sequence[index]
#
#
#
# def inversions_better_elegant(sequence):
#     # More elegant algorithm, but runs around same time as earlier algorithm. Not fast enough for large input sequences
#     number_dict = {}
#     inversions = 0
#     for val in sequence:
#         print(sorted(number_dict.keys()))
#         for key in number_dict:
#             if key > val:
#                 inversions += number_dict[key]
#         if val in number_dict:
#             number_dict[val] += 1
#         else:
#             number_dict[val] = 1
#     return inversions
#
#
# def inversions_better(sequence):
#     # Correct and more efficient than naive, but not fast enough for large input sequences
#     def calc_max_indices(elements):
#         # Single pass to find all index values of the max value in a list
#         if not elements:
#             return []
#         max_indices = []
#         max = elements[0]
#         for i, value in enumerate(elements):
#             if value < max:
#                 continue
#             elif value == max:
#                 max_indices.append(i)
#             else:
#                 max = value
#                 max_indices = [i]
#         return max, max_indices
#
#     # Initialize inversion count
#     inversions = 0
#
#     while True:
#         # Calculate the current max value and all the indices where the max is located
#         max_val, max_index_list = calc_max_indices(sequence)
#
#         # Used to calculate the number of inversion
#         seq_length = len(sequence)
#         index_length = len(max_index_list)
#
#         # End check to exit while loop when all maxes have been accounted for
#         if seq_length <= index_length:
#             return inversions
#
#         for index_val in max_index_list:
#             # print(f"Max_val: ", max_val)
#             # print(f"Max_index_list: ", max_index_list)
#             # print(f"Sequence: ", sequence)
#             # print(f"Inversions: ", inversions)
#
#             # Subtract duplicates from sequence length, the get the range from max index to end of sequence
#             inversions += ((seq_length - index_length) - index_val)
#
#             # Prepare for next iteration
#             index_length -= 1
#
#         # # Remove the current max value from the original sequence, preparing for next iteration with smaller list
#         # sequence.remove(max_val)
#
#         for index in reversed(max_index_list):
#             del sequence[index]
#

# Started naive solution, used to check the accuracy of the above models
def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        # Debug print statements
        # print("i: {0}, j: {1}".format(i, j))
        # print("a[i]: {0}, a[j]: {1}".format(a[i], a[j]))
        if a[i] > a[j]:
            # print("Inversion!")
            number_of_inversions += 1
    return number_of_inversions


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    # print(inversions_naive(elements))
    # print(inversions_better(elements))
    # print(inversions_better_elegant(elements))
    # print(inversions_second_best(elements))

    # print(inversions_recursive_divide(elements))
    print(inversion_count_mergesort(elements))

