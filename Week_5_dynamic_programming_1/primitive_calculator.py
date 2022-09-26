def add_one(n):
    return n + 1


def double(n):
    return n * 2


def triple(n):
    return n * 3


def compute_operations(n):

    # Function list (plus 1, double, triple)
    # First value in tuple used to check if operation can be made
    # Second value in tuple is a function will be used to check the previous number's value
    funct_list = [(1, lambda x: x - 1), (2, lambda x: x / 2), (3, lambda x: x / 3)]

    # Initialize variable to positive infinity
    num_operations = float("inf")

    # Initialize operation count and number sequence dictionaries, add first value
    num_ops_dict = {1: 1}
    num_seq_dict = {1: [1]}

    # Begin calculating all numbers optimal number of operations and the sequence of numbers to get there
    for number in range(2, n + 1):
        # Initialize operation number to positive infinity
        num_ops_dict[number] = float("inf")

        # Loop through each function, checks if operation can be made and the previous value info
        for funct in funct_list:
            if number % funct[0] == 0:
                prev_num_ops = num_ops_dict[funct[1](number)]
                num_operations = prev_num_ops + 1

                # Check for number of operations, save smallest value
                if num_operations < num_ops_dict[number]:
                    num_ops_dict[number] = num_operations

                    # Update the number sequence only if number of operations is better than previous
                    num_seq_dict[number] = num_seq_dict[funct[1](number)] + [number]

    # Catches edge case of n = 1
    if n == 1:
        number = 1
    return num_seq_dict[number]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
