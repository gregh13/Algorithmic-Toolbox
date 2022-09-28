from sys import stdin


def maximum_gold(capacity, weights):
    def choose_bar(max_cap):
        if max_cap in memoization_dict:
            return memoization_dict[max_cap]

        memoization_dict[max_cap] = 0
        for w in range(max_cap):
            if weights[w] <= max_cap:
                val = choose_bar(w)
            pass

        return choose_bar(max_cap)

    memoization_dict = {}



    return 0


if __name__ == '__main__':
    # input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    input_capacity, n, *input_weights = list(map(int, input().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
