def matrix_dot_vector(
    a: list[list[int | float]], b: list[int | float]
) -> list[int | float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    if len(a[0]) != len(b):
        return -1
    res = [sum([i * j for i, j in zip(row, b)]) for row in a]
    return res


# Test Cases
# Test Case 1
print(matrix_dot_vector([[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3]))
print([14, 25, 49])

# Test Case 2
print(matrix_dot_vector([[1, 2], [2, 4], [6, 8], [12, 4]], [1, 2, 3]))
print(-1)

# Test Case 3
print(matrix_dot_vector([[1.5, 2.5], [3.0, 4.0]], [2, 1]))
print([5.5, 10.0])
