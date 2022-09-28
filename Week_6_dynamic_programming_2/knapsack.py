from sys import stdin


def maximum_gold(capacity, weights):
    def choose_bar(max_cap, weight_list):
        if max_cap in memoization_dict:
            return memoization_dict[max_cap]

        memoization_dict[max_cap] = 0
        for w in range(max_cap):
            for i in range(len(weight_list)):
                if weight_list[i] <= max_cap:
                    val = choose_bar(max_cap - weight_list, weight_list[:-1])
                if val > memoization_dict[max_cap]:
                    memoization_dict[max_cap] = val

        return choose_bar(max_cap)

    memoization_dict = {}



    return 0


if __name__ == '__main__':
    # input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    input_capacity, n, *input_weights = list(map(int, input().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
