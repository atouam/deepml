import numpy as np


def reshape_matrix(
    a: list[list[int | float]], new_shape: tuple[int, int]
) -> list[list[int | float]]:
    # Write your code here and return a python list after reshaping by using numpy's tolist() method
    # shape verification
    arr = np.asarray(a)
    if np.prod(new_shape) != np.prod(arr.shape):
        return []

    return np.reshape(arr, new_shape).tolist()


# Test Cases
# Test Case 1
print(reshape_matrix([[1, 2, 3, 4], [5, 6, 7, 8]], (4, 2)))
print([[1, 2], [3, 4], [5, 6], [7, 8]])

# Test Case 2
print(reshape_matrix([[1, 2, 3, 4], [5, 6, 7, 8]], (1, 4)))
print([])

# Test Case 3
print(reshape_matrix([[1, 2, 3], [4, 5, 6]], (3, 2)))
print([[1, 2], [3, 4], [5, 6]])

# Test Case 4
print(reshape_matrix([[1, 2, 3, 4], [5, 6, 7, 8]], (2, 4)))
print([[1, 2, 3, 4], [5, 6, 7, 8]])
