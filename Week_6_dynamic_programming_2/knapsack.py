from sys import stdin


def maximum_gold(capacity, weights):
    def choose_bar(max_cap):
        if max_cap in memoization_dict:
            return memoization_dict[max_cap]

        max_cap_val = 0
        for i in range(len(weights)):
            weight_i = weights[i]
            if weight_i <= max_cap:
                val = choose_bar(max_cap - weight_i) + 1
                if val > max_cap_val:
                    max_cap_val = val

        memoization_dict[max_cap] = max_cap_val
        return memoization_dict[max_cap]

    memoization_dict = {0: 0}
    choose_bar(capacity)
    return memoization_dict[capacity]


if __name__ == '__main__':
    # input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    input_capacity, n, *input_weights = list(map(int, input().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
