def lcs3(first_sequence, second_sequence, third_sequence):
    # Make set for faster verification in steps below
    third_set = set(third_sequence)

    match_list = []

    # Compared sequences item by item, add any matches to list
    for i in range(len(first_sequence)):
        for j in range(len(second_sequence)):
            if first_sequence[i] == second_sequence[j] and first_sequence[i] in third_set:
                # Adds index of item in each sequence, used to eliminate duplicates in next step
                match_list.append([first_sequence[i], j, i])

    for k in range(len(third_sequence)):
        for j in range(len(match_list)):
            if third_sequence[k] == match_list[j][0]:
                match_list[j].append(k)

    match_list_length = len(match_list)
    sequence_count = [1] * match_list_length

    for i in range(match_list_length):
        for j in range(i):

            if match_list[j][1] < match_list[i][1] and sequence_count[i] < (sequence_count[j] + 1) \
                    and match_list[j][2] < match_list[i][2] and match_list[j][3] < match_list[i][3]:
                # Update sequence count to one more than the best recent count
                sequence_count[i] = sequence_count[j] + 1

    return 0

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
