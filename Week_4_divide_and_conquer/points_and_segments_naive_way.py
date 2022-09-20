from sys import stdin


def points_dict(starts, ends, points):
    len_start = len(starts)
    assert len_start == len(ends)
    count = []
    dictionary = {}

    for i in range(len_start):
        for val in range(starts[i], ends[i] + 1):
            if val not in dictionary:
                dictionary[val] = 1
            else:
                dictionary[val] += 1

    for point in points:
        try:
            count.append(dictionary[point])
        except KeyError:
            count.append(0)
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
    # data = list(map(int, stdin.read().split()))
    data = list(map(int, input().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]
    #
    output_count1 = points_cover_naive(input_starts, input_ends, input_points)
    print(*output_count1)
    # output_count = points_naive_better(input_starts, input_ends, input_points)
    # output_count = points_dict(input_starts, input_ends, input_points)
    # print(*output_count)
