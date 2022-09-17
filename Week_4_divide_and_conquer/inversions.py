from itertools import combinations


def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        print(f"i: {0}, j: {1}".format(i, j))
        print(f"a[i]: {0}, a[j]: {1}".format(a[i], a[j]))
        if a[i] > a[j]:
            print("Inversion!")
            number_of_inversions += 1
    return number_of_inversions


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions_naive(elements))
