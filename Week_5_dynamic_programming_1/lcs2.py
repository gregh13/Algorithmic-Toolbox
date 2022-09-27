def lcs2(first_sequence, second_sequence):

    index_match_list = []
    for i in range(len(first_sequence)):
        for j in range(len(second_sequence)):
            if first_sequence[i] == second_sequence[j]:
                index_match_list.append((j, i))

    length_of_index_matches = len(index_match_list)
    sequence_count = [1] * length_of_index_matches

    for i in range(length_of_index_matches):
        for j in range(i):
            if index_match_list[j][0] < index_match_list[i][0] and sequence_count[i] < (sequence_count[j] + 1)\
                    and index_match_list[j][1] != index_match_list[i][1]:
                sequence_count[i] = sequence_count[j] + 1

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

    print(lcs2(a, b))
