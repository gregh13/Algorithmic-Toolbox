# Quick Sort and Quick3 Sort

# Goal: Design an improved quick sort algorithm to handle cases with lots of duplicate values.
#       The input is an array of integers that need to be sorted, returns the sorted array.


from random import randint


def partition3(array, left, right):
    # My implementation of the Quick3 sorting algorithm
    # print("\nNew Batch")
    mid_1 = left        # left bound of same block
    mid_2 = left + 1    # right bound of same block
    pivot = array[left]
    for i in range(left, right):
        # Debugging statements
        # print("Pivot: ", pivot)
        # print("Mid_1: ", mid_1)
        # print("Mid_2: ", mid_2)
        # print("array[i+1]: ", array[i+1])
        # print("Array Before: ", array[left:right+1])
        if array[i+1] == pivot:
            array[mid_2], array[i+1] = array[i+1], array[mid_2]
            mid_2 += 1
        if array[i+1] < pivot:
            # Found number less than pivot element, perform swap to add block to "smaller than" section
            array[mid_1], array[i+1] = array[i+1], array[mid_1]
            # Swap again to return the duplicate pivot value back
            array[mid_2], array[i+1] = array[i+1], array[mid_2]
            # Update the index for the mid-block
            mid_1 += 1
            mid_2 += 1
        # print("Array After:  ", array[left:right+1])
        # print("---------------")

    return mid_1, mid_2


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    # swap random index to the start of list as the pivot element
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1)
    randomized_quick_sort(array, m2, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
