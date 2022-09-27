def lcs2(first_sequence, second_sequence):

    first_length = len(first_sequence)
    second_length = len(second_sequence)

    index_match_list = []
    for i in range(first_length):
        for j in range(second_length):
            if first_sequence[i] == second_sequence[j]:
                index_match_list.append(j)

    length_of_index_matches = len(index_match_list)
    sequence_count = [1] * length_of_index_matches

    for i in range(length_of_index_matches):
        for j in range(i):
            if index_match_list[j] < index_match_list[i] and sequence_count[i] < (sequence_count[j] + 1):
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
