def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def find_min_max(start_index, end_index):
    min_value = float("-inf")
    max_value = float("inf")
    print(min_value, max_value)

    for k in range(start_index, end_index - 1):
        a = maximum_vals[]
    return 0, 1


def maximum_value(digits, operators, num_digits):
    for i in range(num_digits):
        minimum_vals[i][i] = digits[i]
        maximum_vals[i][i] = digits[i]

    # Loops through all index pairs combos ( [0,0] [1,1] --> [0,3] [1,4] etc)
    for s in range(num_digits - 1):
        for i in range(num_digits - s):
            j = i + s
            minimum_vals[i][j], maximum_vals[i][j] = find_min_max(i, j)
    return maximum_vals[0][num_digits-1]



if __name__ == "__main__":
    input_data = list(input().split())
    length = len(input_data)
    n_raw = (length - 1) / 2
    n = int(n_raw)
    assert float(n) == n_raw

    digit_sequence, operator_sequence = input_data[0:2 * n + 1:2], input_data[1:2 * n:2]
    n_digits = n + 1
    minimum_vals = [[None] * n_digits for x in range(n_digits)]
    maximum_vals = [[None] * n_digits for x in range(n_digits)]

    print(maximum_value(digit_sequence, operator_sequence, n_digits))
