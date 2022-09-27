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
