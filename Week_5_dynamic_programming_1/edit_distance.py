def edit_distance(first_string, second_string):

    # Add dummy initial variable to help string index and loop index match
    first_string = "0" + first_string
    second_string = "0" + second_string


    first_length = len(first_string)
    second_length = len(second_string)

    # Create 2d matrix with first string chars as the rows and first second string char as the columns
    string_matrix = [[0 for x in range(second_length)] for y in range(first_length)]


    for j in range(1, second_length):
        # Initialize the starting number of actions taken to get to column j
        string_matrix[0][j] = j

        for i in range(1, first_length):
            # Initialize the starting number of actions taken to get to row i
            string_matrix[i][0] = i

            # Compute the total number of actions for each possible next step
            insertion = string_matrix[i][j-1] + 1
            deletion = string_matrix[i-1][j] + 1
            match = string_matrix[i-1][j-1]
            mismatch = string_matrix[i-1][j-1] + 1

            # Save number of actions for next step (options depend on if letters are a match or mismatch)
            if first_string[i] == second_string[j]:
                string_matrix[i][j] = min(insertion, deletion, match)
            else:
                string_matrix[i][j] = min(insertion, deletion, mismatch)

    return string_matrix[first_length-1][second_length-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
