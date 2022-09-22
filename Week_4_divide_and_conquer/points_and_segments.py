from sys import stdin


class Interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    # Used to print out specific node range, not needed for this challenge (but useful in the real world!)
    # def __str__(self):
    #     return "[" + str(self.low) + "," + str(self.high) + "]"


class Node:
    def __init__(self, range, max):
        self.range = range
        self.max = max
        self.left = None
        self.right = None

    # Used to print out tree order, not needed for this challenge (but useful in the real world!)
    # def __str__(self):
    #     return "[" + str(self.range.low) + ", " + str(self.range.high) + "] " + "max = " + str(self.max) + "\n"


# Used to build the interval tree
def insert(root, x):
    # root is a Node object with range (Interval), max (int), left (Node), and right (Node) attributes
    # x is an Interval object with low (int) and high (int) attributes
    if root == None:
        return Node(x, x.high)

    # Sort by lowest value in interval
    if x.low < root.range.low:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)

    # Update max value for the parent node
    if root.max < x.high:
        root.max = x.high

    return root


# Create a balanced tree:
# sort segments by start value
def interval_tree(starts, ends, points):
    sorted_segments = sorted(zip(starts, ends))
    print(sorted_segments)

    def build_tree(root, sequence):
        seq_length = len(sequence)
        if seq_length < 2:
            if sequence:
                # add Node
                insert(root, Interval(sequence[0][0], sequence[0][1]))
                return
            else:
                # Empty list
                return

        mid = seq_length // 2
        insert(root, Interval(sequence[mid]))
        build_tree(root, sequence[:mid])
        build_tree(root, sequence[mid+1:])


















def points_dict(starts, ends, points):
    len_start = len(starts)
    assert len_start == len(ends)
    count = [0] * len(points)
    dictionary = {}

    for start, end in zip(starts, ends):
        for val in range(start, end + 1):
            if val not in dictionary:
                dictionary[val] = 1
            else:
                dictionary[val] += 1

    for index, point in enumerate(points):
        if point in dictionary:
            count[index] = dictionary[point]

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
    output_count = points_dict(input_starts, input_ends, input_points)
    # output_count = points_counter(input_starts, input_ends, input_points)
    print(*output_count)
