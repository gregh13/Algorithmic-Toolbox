from sys import stdin


def points_dict_reversed(starts, ends, points):
    len_start = len(starts)
    assert len_start == len(ends)
    count = [0] * len(points)
    points_set = set(points)
    dictionary = {p: 0 for p in points_set}

    for i in range(len_start):
        for point in points_set:
            if starts[i] <= point <= ends[i]:
                dictionary[point] += 1

    for index, point in enumerate(points):
        count[index] = dictionary[point]

    return count


def points_dict(starts, ends, points):
    len_start = len(starts)
    assert len_start == len(ends)
    count = [0] * len(points)
    dictionary = {}

    for i in range(len_start):
        for val in range(starts[i], ends[i] + 1):
            if val not in dictionary:
                dictionary[val] = 1
            else:
                dictionary[val] += 1

    for index, point in enumerate(points):
        if point in dictionary:
            count[index] = dictionary[point]

    return count


def points_naive_better(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for start, end in zip(starts, ends):
        for index, point in enumerate(points):
            if start > point:
                continue
            if end < point:
                continue
            if start <= point <= end:
                count[index] += 1
    return count


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_dict(input_starts, input_ends, input_points)
    print(*output_count)
