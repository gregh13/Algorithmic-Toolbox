# Simple Binary Search Problem (with duplicates)

# Goal: Design a basic binary search algorithm that given inputs of a list of keys to sort through and queries to
#       search, will return the index for the list of keys that holds the query. If not in list, returns -1
#       Note: Index returned must be the first occurance of a number, not any of the duplicates


def binary_search(keys, query):
    # My simple binary search
    def my_search(keys, query, left, right):
        # print("Key Range: ", keys[left:right])
        # print("Left: ", left)
        # print("Right: ", right)
        # Termination Check
        if left >= right:
            # Query not found in list
            return -1

        # Gets the floored midpoint
        mid = (left + right) // 2
        mid_val = keys[mid]
        if query == mid_val:
            # Now we need to return the first index that matches the query
            if right - left <= 2:
                if keys[left] == query:
                    return left
                else:
                    return mid
            else:
                return my_search(keys, query, left, mid+1)

            # This approach works well, but is too slow for very large arrays with many duplicates
            # while keys[mid] == query:
            #     if mid == 0:
            #         return mid
            #     mid -= 1
            # return mid + 1
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
