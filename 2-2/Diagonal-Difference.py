def diagonalDifference(arr):
    primary_diagonal = []
    secondary_diagonal = []
    for i in range(0, len(arr)):
        primary_diagonal.append(arr[i][i])
        secondary_diagonal.append(arr[i][-i-1])

    primary_diagonal_sum = sum(primary_diagonal)
    secondary_diagonal_sum = sum(secondary_diagonal)

    diagonal_difference = abs(primary_diagonal_sum - secondary_diagonal_sum)

    return diagonal_difference

