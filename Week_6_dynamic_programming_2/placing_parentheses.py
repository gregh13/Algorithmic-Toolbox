def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def maximum_value(digits, operators):
    number_of_digits = len(digits)
    minimum_vals = [[None] * number_of_digits for x in range(number_of_digits)]
    maximum_vals = [[None] * number_of_digits for x in range(number_of_digits)]
    print(minimum_vals)
    print(maximum_vals)
    for i in range(number_of_digits):
        minimum_vals[i][i] = digits[i]
        maximum_vals[i][i] = digits[i]
    print(minimum_vals)
    print(maximum_vals)
    return 0


if __name__ == "__main__":
    input_data = list(input().split())
    length = len(input_data)
    n_raw = (length - 1) / 2
    n = int(n_raw)
    assert float(n) == n_raw

    digit_sequence, operator_sequence = input_data[0:2 * n + 1:2], input_data[1:2 * n:2]

    print(maximum_value(digit_sequence, operator_sequence))
