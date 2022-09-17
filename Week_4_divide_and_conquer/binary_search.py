# Simple Binary Search Problem

# Goal: Design a basic binary search algorithm that given inputs of a list of keys to sort through and queries to
#       search, will return the index for the list of keys that holds the query. If not in list, returns -1


def binary_search(keys, query):
    # My simple binary search
    def my_search(keys, query, left, right):
        # Termination Check
        if left >= right:
            # Query not found in list
            return -1

        # Gets the floored midpoint
        mid = (left + right) // 2
        mid_val = keys[mid]
        if query == mid_val:
            return mid
        elif query < mid_val:
            return my_search(keys, query, left, mid)
        else:
            return my_search(keys, query, mid+1, right)
    return my_search(keys, query, 0, len(keys))


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
