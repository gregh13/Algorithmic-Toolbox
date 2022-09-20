from sys import stdin


def points_naive_better(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for i in range(starts):
        for j in range(points):
            if starts[i] > points[j]:
                continue
            if points[j] < ends[i]:
                continue
            if starts[i] <= points[j] <= ends[i]:
                count[j] += 1
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

    # output_count = points_cover_naive(input_starts, input_ends, input_points)
    output_count = points_naive_better(input_starts, input_ends, input_points)
    print(*output_count)