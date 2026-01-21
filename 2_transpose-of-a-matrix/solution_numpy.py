def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    b = []
    for row in range(len(a[0])):
        b.append([line[row] for line in a])
    return b


# Test Cases
# Test Case 1
print(transpose_matrix([[1, 2], [3, 4], [5, 6]]))
print([[1, 3, 5], [2, 4, 6]])

# Test Case 2
print(transpose_matrix([[1, 2, 3], [4, 5, 6]]))
print([[1, 4], [2, 5], [3, 6]])
