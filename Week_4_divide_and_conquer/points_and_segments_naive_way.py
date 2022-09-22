from sys import stdin


def points_counter(starts, ends, points):
    assert len(starts) == len(ends)
    point_length = len(points)
    count = [0] * point_length
    sorted_points_list = [i for _, i in sorted(zip(points, range(len(points))))]

    joined_list = [(point, 1) for point in points]
    joined_list.extend([(start, 0) for start in starts])
    joined_list.extend([(end, 2) for end in ends])
    joined_list.sort()
    # print("Joined List: ", joined_list)

    segs_and_points = 0
    i = 0
    for _, p_type in joined_list:
        if p_type == 0:
            segs_and_points += 1
        elif p_type == 2:
            segs_and_points -= 1
        else:
            count[sorted_points_list[i]] = segs_and_points
            i += 1
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
    # data = list(map(int, input().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]
    #
    # output_count1 = points_cover_naive(input_starts, input_ends, input_points)
    # print(*output_count1)

    output_count = points_counter(input_starts, input_ends, input_points)
    print(*output_count)
