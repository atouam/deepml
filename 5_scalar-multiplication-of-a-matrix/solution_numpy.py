def scalar_multiply(
    matrix: list[list[int | float]], scalar: int | float
) -> list[list[int | float]]:
    return [[e * scalar for e in row] for row in matrix]


# Test Cases
# Test Case 1
print(scalar_multiply([[1, 2], [3, 4]], 2))
print([[2, 4], [6, 8]])

# Test Case 2
print(scalar_multiply([[0, -1], [1, 0]], -1))
print([[0, 1], [-1, 0]])
