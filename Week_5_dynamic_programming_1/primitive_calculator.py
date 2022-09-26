def add_one(n):
    return n + 1


def double(n):
    return n * 2


def triple(n):
    return n * 3


def compute_operations(n):

    # Function list (plus 1, double, triple)
    funct_list = [(1, lambda x: x - 1), (2, lambda x: x / 2), lambda x: x / 3]

    num_operations = float("inf")

    num_ops_dict = {1: 1}
    num_seq_dict = {1: [1]}

    for number in range(2, n + 1):

        num_ops_dict[number] = float("inf")

        for funct in funct_list:
            if number % funct[0] == 0:
                prev_num_ops = num_ops_dict[funct[1](number)]
                num_operations = prev_num_ops + 1

                if num_operations < num_ops_dict[number]:
                    num_ops_dict[number] = num_operations

                    num_seq_dict[number] = num_seq_dict[funct[1](number)] + [number]

    return num_seq_dict[number]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
