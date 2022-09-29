from sys import stdin


def partition3(values):
    def find_split(value_list, remaining_sum):
        if remaining_sum in memoization_dict:
            return memoization_dict[remaining_sum]

        # Initialize value
        possible_path = False

        # Loop through all possible values
        for i in range(len(value_list)):
            i_value = value_list[i]

            # Check is item is small enough to select
            if i_value <= remaining_sum:

                # Check next optimal choice if i_value is picked (remove i_value from list of values too)
                possible_path = find_split((value_list[:i] + value_list[i+1:]), remaining_sum - i_value)

                # If a way to split the items into the share_value exists, stop looking any further
                if possible_path:
                    break
                else:
                    # Continue searching
                    continue

        memoization_dict[remaining_sum] = possible_path
        return possible_path

    # Initialize variable
    can_split_evenly = False

    # This number is given by the problem set
    ways_to_split = 3

    # Calculate total value of all items
    val_sum = sum(values)

    # Check if even possible to split the sum into the number of parts desired
    if val_sum % ways_to_split != 0:
        return can_split_evenly

    # Check if there are enough individual pieces to split it correctly
    if 0 < len(values) < ways_to_split:
        return can_split_evenly

    share_value = val_sum / ways_to_split

    values.sort(reverse=True)

    # Check if the largest item is greater than the share_value (if so, not possible to split evenly)
    if values[0] > share_value:
        return can_split_evenly

    # Check list numbers of times needed to split
    for n in range(ways_to_split):

        # Initialize dictionary
        memoization_dict = {0: True}

        # Start recursive memoization call
        can_split_evenly = find_split(values, share_value)

        # If no possible path, can't split evenly
        if not can_split_evenly:
            break
        else:
            # One possible path found, need to remove those items for the next iteration
            value_path = [int(key) for key, value in memoization_dict.items() if value is True]
            for i in range(1, len(value_path)):
                used_value = value_path[i] - value_path[i-1]
                values.remove(used_value)

    return can_split_evenly


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    # input_n, *input_values = list(map(int, input().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
