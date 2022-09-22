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
    def __str__(self):
        return "[" + str(self.range.low) + ", " + str(self.range.high) + "] " + "max = " + str(self.max) + "\n"


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


def inOrder(root):
    if root == None:
        return

    inOrder(root.left)
    print(root, end="")
    inOrder(root.right)


# Create a balanced tree:
# sort segments by start value
def interval_tree(starts, ends, points):
    def build_tree(root, sequence):
        # print("Root: ", root)
        # print("Sequence: ", sequence)
        seq_length = len(sequence)
        if seq_length < 2:
            if sequence:
                # add Node
                # print("Seq == 1")
                root = insert(root, Interval(sequence[0][0], sequence[0][1]))
                return root
            else:
                # print("Empty Seq")
                # Empty list
                return None

        mid = seq_length // 2
        root = insert(root, Interval(sequence[mid][0], sequence[mid][1]))
        build_tree(root, sequence[:mid])
        build_tree(root, sequence[mid+1:])
        inOrder(root)
        return root

    def calc_point_counter(root, point):
        # Add to point_counter if within segment start and end
        print("Point: ", point)
        print("Counter Before: ", point_counter[0])
        print("Root Range: ", root.range.low, root.range.high)
        print("Root Left: ", root.left)
        print("Root Right: ", root.right)
        if root.range.low <= point <= root.range.high:
            point_counter[0] += 1
        print("Counter After: ", point_counter[0])

        # Check child nodes recursively for other segments
        if root.left is not None and root.left.max >= point:
            print("Go left")
            calc_point_counter(root.left, point)

        # Left branch is exhausted, check right branch
        if root.right is not None:
            print("Go Right")
            calc_point_counter(root.right, point)

        print("Done")
        # All branches and leaves checked
        return

    assert len(starts) == len(ends)

    # Initialize count array
    count = [0] * len(points)

    # Sort segments for more balanced interval tree
    sorted_segments = sorted(zip(starts, ends))
    # print(sorted_segments)

    # Build interval tree
    root = build_tree(None, sorted_segments)

    # Search tree for each point and calculate count for each point
    for index, point in enumerate(points):
        point_counter = [0]
        calc_point_counter(root, point)
        count[index] = point_counter[0]

    return count
















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
    data = list(map(int, input().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]
    # output_count = points_cover_naive(input_starts, input_ends, input_points)
    # output_count = points_dict(input_starts, input_ends, input_points)
    # output_count = points_counter(input_starts, input_ends, input_points)
    # print(*output_count)

    output_count = interval_tree(input_starts, input_ends, input_points)
    print(*output_count)
