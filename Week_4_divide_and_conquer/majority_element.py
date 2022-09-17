# Majority Element Present Problem

# Goal: Design a search algorithm that given an input of a list of integers, will check if there is a value that appears
#       more than 50% of the time in the array (i.e. has the majority). Returns a 1 if true, 0 for false

def majority_element_my_way(elements):
    # Can handle very large arrays
    # Similar to count sort, but more versatile as range of numbers doesn't need to be small or even known beforehand
    unique_element_dict = {}
    majority_size = len(elements) / 2
    for item in elements:
        if item not in unique_element_dict:
            unique_element_dict[item] = 1
        else:
            unique_element_dict[item] += 1
    if max(unique_element_dict.values()) > majority_size:
        return 1
    return 0

    # Still not fast enough for very large inputs
    # This adds the feature that if more than 50% of items in array have been counted, then not possible
    # total_count = 0
    # half_size_of_elements = len(elements) / 2
    # checked_elements = []
    # for e in elements:
    #     if e not in checked_elements:
    #         checked_elements.append(e)
    #         element_count = elements.count(e)
    #         if element_count > half_size_of_elements:
    #             return 1
    #         # Check to see if 50% of elements already reached, can abort
    #         total_count += element_count
    #         if total_count > half_size_of_elements:
    #             return 0
    # return 0

    # This is better, but still not good enough for large inputs
    # This makes sure to not re-check any values in array
    # checked_elements = []
    # for e in elements:
    #     if e not in checked_elements:
    #         checked_elements.append(e)
    #         if elements.count(e) > len(elements) / 2:
    #             return 1
    # return 0


# def majority_element_naive(elements):
#     # For large arrays, this method is much too slow.
#     # Checks every item, even if it already checked that value before
#     for e in elements:
#         if elements.count(e) > len(elements) / 2:
#             return 1
#     return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    # print(majority_element_naive(input_elements))
    print(majority_element_my_way(input_elements))
