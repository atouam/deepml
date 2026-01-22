def mean_list(lst: list[float]) -> float:
    return sum(lst) / len(lst)


def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == "row":
        means = [mean_list(row) for row in matrix]
    elif mode == "column":
        means = [mean_list(col) for col in zip(*matrix)]
    else:
        raise ValueError("Invalid mode. Use 'row' or 'column'.")
    return means


# Test Cases
# Test Case 1
print(calculate_matrix_mean([[1, 2, 3], [4, 5, 6], [7, 8, 9]], "column"))
print([4.0, 5.0, 6.0])

# Test Case 2
print(calculate_matrix_mean([[1, 2, 3], [4, 5, 6], [7, 8, 9]], "row"))
print([2.0, 5.0, 8.0])
