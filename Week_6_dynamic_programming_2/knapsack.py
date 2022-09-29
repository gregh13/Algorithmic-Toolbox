from sys import stdin


def maximum_gold(capacity, weights):
    def choose_bar(max_cap, weight_list):
        if max_cap in memoization_dict:
            return memoization_dict[max_cap]

        # Initialize value
        max_cap_val = 0

        # Loop through all possible weight values
        for i in range(len(weight_list)):
            weight_i = weight_list[i]

            # Check if object is too heavy to pick
            if weight_i <= max_cap:
                # Find next optimal choice if weight_i chosen (removed from weight list as well)
                val = choose_bar(max_cap - weight_i, (weight_list[:i] + weight_list[i+1:])) + weight_i
                if val > max_cap_val:
                    # Save more optimal value
                    max_cap_val = val

        # Update dictionary to value (either 0 or val from loop)
        memoization_dict[max_cap] = max_cap_val
        return memoization_dict[max_cap]

    # Sort weights into increasing order
    weights.sort()

    # Initialize dictionary
    memoization_dict = {0: 0}

    # Start recursive memoization call
    choose_bar(capacity, weights)

    return memoization_dict[capacity]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    # input_capacity, n, *input_weights = list(map(int, input().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
