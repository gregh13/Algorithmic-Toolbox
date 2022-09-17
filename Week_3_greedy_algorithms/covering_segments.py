# Collecting Signatures (Covering Segments by Points) Problem

# Goal: Design an algorithm that given inputs of the number of segments and list of start/end for the segments,
#       returns a list of the least number of points that include every segment.
#       Note: Segments can be a single point (3, 3) and can repeat in the input


from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    # Optimized greedy way
    if not segments:
        return "Must input at least one segment!"
    # Sorts segments in ascending order from the second value in the tuple (end value)
    segments.sort(key=lambda x: x[1])
    # Initialize points list with end of first segment
    points = [segments[0][1]]
    for s in segments:
        if s.start <= points[-1] <= s.end:
            continue
        points.append(s.end)

    return points


    # Greedy way - slower than needs to be by checking through the range of each segment
    # if not segments:
    #     return "Must input at least one segment!"
    # # Sorts segments in ascending order from the second value in the tuple (end value)
    # segments.sort(key=lambda x: x[1])
    # # Initialize points list with end of first segment
    # points = [segments[0][1]]
    # for s in segments:
    #     if points[-1] not in range(s.start, s.end + 1):
    #         points.append(s.end)
    # return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    # n, *data = map(int, input().split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
