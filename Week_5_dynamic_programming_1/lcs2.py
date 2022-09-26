def lcs2(first_sequence, second_sequence):

    first_length = len(first_sequence) + 1
    second_length = len(second_sequence) + 1

    # Create 2d matrix with first seq numbers as the columns and second seq numbers as the rows
    # Initialize all values to 0 as this will be our 'memory' array
    seq_2d_array = [[0 for x in range(len(first_sequence))] for y in range(len(second_sequence))]

    for i in range(first_length):
        points_to_add = 0
        for j in range(second_length):
            if first_sequence[i] == second_sequence[j]:
                points_to_add = 1
            seq_2d_array[i][j] = seq_2d_array[i][j-1] + points_to_add

    return 0


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
