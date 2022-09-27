def lcs3(first_sequence, second_sequence, third_sequence):

    first_sequence = [x for x in first_sequence if x in set(second_sequence) and x in set(third_sequence)]
    second_sequence = [y for y in second_sequence if y in first_sequence]
    third_sequence = [z for z in third_sequence if z in first_sequence]
    match_list = []

    # Compared sequences item by item, add any matches to list
    for i in range(len(first_sequence)):
        first = first_sequence[i]
        for j in range(len(second_sequence)):
            if first == second_sequence[j]:
                for k in range(len(third_sequence)):
                    if first == third_sequence[k]:
                        match_list.append((j, i, k))

    match_list_length = len(match_list)
    sequence_count = [1] * match_list_length

    for i in range(match_list_length):
        for j in range(i):
            if match_list[j][0] < match_list[i][0] and sequence_count[i] < (sequence_count[j] + 1) \
                    and match_list[j][1] < match_list[i][1] and match_list[j][2] < match_list[i][2]:
                # Update sequence count to one more than the best recent count
                sequence_count[i] = sequence_count[j] + 1

    # In case no matches and sequence_count is empty list
    max_count = 0
    if sequence_count:
        max_count = max(sequence_count)
    return max_count


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
