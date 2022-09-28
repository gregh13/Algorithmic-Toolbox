from sys import stdin


def partition3(values):
    can_split_evenly = False

    ways_to_split = 3
    val_sum = sum(values)
    if val_sum % ways_to_split != 0:
        return can_split_evenly

    share_value = val_sum / ways_to_split

    return can_split_evenly


if __name__ == '__main__':
    # input_n, *input_values = list(map(int, stdin.read().split()))
    input_n, *input_values = list(map(int, input().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
