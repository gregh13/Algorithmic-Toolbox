from sys import stdin


def partition3(values):
    def find_split(value_list, remaining_sum):
        if remaining_sum in memoization_dict:
            return memoization_dict[remaining_sum]

        val = 0
        for i in range(len(value_list)):
            i_value = value_list[i]
            if i_value <= remaining_sum:
                sequence = find_split(value_list[1:], remaining_sum - i_value) + i_value



    can_split_evenly = False

    ways_to_split = 3
    val_sum = sum(values)
    if val_sum % ways_to_split != 0:
        return can_split_evenly

    if 0 < len(values) < ways_to_split:
        return can_split_evenly

    share_value = val_sum / ways_to_split

    values.sort()
    memoization_dict = {0: 0}
    for n in range(ways_to_split):
        find_split(values, share_value)



    return can_split_evenly


if __name__ == '__main__':
    # input_n, *input_values = list(map(int, stdin.read().split()))
    input_n, *input_values = list(map(int, input().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
