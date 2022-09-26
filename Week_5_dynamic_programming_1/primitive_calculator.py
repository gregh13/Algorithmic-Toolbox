def add_one(n):
    return n + 1

def double(n):
    return n * 2

def triple(n):
    return n * 3


def compute_operations(n):
    # Initialize output list
    output_seq = [1]

    # Function list (plus 1, double, triple)
    funct_list = [lambda x: x + 1, lambda x: x * 2, lambda x: x * 3]

    num_operations = float("inf")

    min_number_ops = {0: 0}

    for number in range(1, n + 1):
        min_number_ops[number] = float("inf")

        for funct in funct_list:
            if number >= funct(output_seq[-1]):
                num_operations = min_number_ops[output_seq[-1]] + 1

    return output_seq


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
