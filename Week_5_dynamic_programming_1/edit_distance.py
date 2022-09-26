def edit_distance(first_string, second_string):
    first_string = "x" + first_string
    second_string = "x" + second_string
    first_length = len(first_string)
    second_length = len(second_string)

    # Create 2d matrix
    string_matrix = [[0 for x in range(second_length)] for y in range(first_length)]

    for j in range(1, second_length):
        string_matrix[0][j] = j
        for i in range(1, first_length):
            string_matrix[i][0] = i

            insertion = string_matrix[i][j-1] + 1
            deletion = string_matrix[i-1][j] + 1
            match = string_matrix[i-1][j-1]
            mismatch = string_matrix[i-1][j-1] + 1

            if first_string[i] == second_string[j]:
                string_matrix[i][j] = min(insertion, deletion, match)
            else:
                string_matrix[i][j] = min(insertion, deletion, mismatch)

    return string_matrix[first_length-1][second_length-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
