def lcs2(first_sequence, second_sequence):

    first_length = len(first_sequence)
    second_length = len(second_sequence)

    sequence_count = []
    index_match = []
    for i in range(first_length):
        for j in range(second_length):
            if first_sequence[i] == second_sequence[j]:
                index_match.append(j)





    return


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
