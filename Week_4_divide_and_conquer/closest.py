from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def min_squared_divide_and_conquer(points):
    def recur_divide(point_list, min_dist):

        list_length = len(point_list)

        if list_length <= 2:
            if list_length == 2:
                # Check for smaller distances
                min_dist = min(min_dist, distance_squared(point_list[0], point_list[1]))

                # Sort two points by y value
                point_list.sort(key=lambda p: p[1])

            return min_dist, point_list

        mid = list_length // 2
        min_dist_left, sorted_y_left = recur_divide(point_list[:mid], min_dist)
        min_dist_right, sorted_y_right = recur_divide(point_list[mid:], min_dist)

        # Get the smallest distance
        min_dist = min(min_dist_left, min_dist_right)

        # Get x-value that was used as the dividing line
        mid_x_val = point_list[mid].x

        # Merge both sorted_y lists
        sorted_y_all = []
        while sorted_y_right and sorted_y_left:
            a = sorted_y_left[0][1]
            b = sorted_y_right[0][1]
            if a < b:
                sorted_y_all.append(sorted_y_left.pop(0))
            else:
                sorted_y_all.append(sorted_y_right.pop(0))

        # Add the rest of either list (since one will be exhausted above)
        sorted_y_all.extend([i for i in sorted_y_left])
        sorted_y_all.extend([i for i in sorted_y_right])

        # Filter out points too far away for the next comparison
        possible_points = [point for point in sorted_y_all if abs(point.x - mid_x_val) <= min_dist]

        # Now sort new list by y value
        # possible_points.sort(key=lambda point: point[1])

        # Check point by point for any smaller squared distances
        # Start value used to reduce nested loop list length
        start = 1
        for point1 in possible_points:
            for point2 in possible_points[start:]:
                # Any two points that have a difference in y greater than the min_dist need not be considered
                if abs(point1.y - point2.y) > min_dist:
                    # Since it is sorted by y, that means all numbers after are too far away
                    break
                else:
                    # Calculate distance
                    min_dist = min(min_dist, distance_squared(point1, point2))

            # Move start forward for inner loop splice
            start += 1
        return min_dist

    # Sort points by x value, add index value for y sort matching within recursive calls
    points.sort()

    # Initialize min_distance to positive infinity
    min_distance = float("inf")

    # Call recursive divide and conquer function
    min_distance = recur_divide(points, min_distance)

    return min_distance


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    # set1 = input_points
    # set2 = input_points
    # print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(set1))))
    print("{0:.9f}".format(sqrt(min_squared_divide_and_conquer(input_points))))

