def calculate_eigenvalues(matrix: list[list[float | int]]) -> list[float]:
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    delta = (a + d) ** 2 + 4 * (b * c - a * d)
    if delta < 0:
        raise ValueError("Matrix has complex eigenvalues")
    sqrt_delta = (delta) ** 0.5
    eigenvalues = [(a + d + sqrt_delta) / 2, (a + d - sqrt_delta) / 2]
    return eigenvalues


# Test Cases
# Test Case 1
print(calculate_eigenvalues([[2, 1], [1, 2]]))
print([3.0, 1.0])

# Test Case 2
print(calculate_eigenvalues([[4, -2], [1, 1]]))
print([3.0, 2.0])
