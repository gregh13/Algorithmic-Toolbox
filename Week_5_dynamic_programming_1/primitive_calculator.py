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
    funct_list = [(1, lambda x: x - 1), (2, lambda x: x / 2), lambda x: x / 3]

    num_operations = float("inf")

    num_ops_dict = {1: (1, [1])}

    for number in range(1, n + 1):
        # Initialize output list
        output_seq = [1]

        num_ops_dict[number] = (float("inf"), output_seq)

        for funct in funct_list:
            if number % funct[0] == 0:
                prev_values = num_ops_dict[funct[1](number)]
                num_operations = prev_values[0] + 1
                output_seq = prev_values[1]

                if num_operations < num_ops_dict[number]:
                    num_ops_dict[number][0] = num_operations

                    num_ops_dict[number][1] = prev_values[1] + [number]

    return output_seq


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
