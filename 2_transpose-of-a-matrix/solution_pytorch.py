import torch


def transpose_matrix(a) -> torch.Tensor:
    """
    Transpose a 2D matrix `a` using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a transposed tensor.
    """
    a_t = torch.as_tensor(a)
    return a_t.T


# Test Cases
# Test Case 1
res = transpose_matrix(torch.tensor([[1, 2, 3], [4, 5, 6]]))
print(res.numpy().tolist())
print([[1, 4], [2, 5], [3, 6]])

# Test Case 2
res = transpose_matrix(torch.tensor([[1, 2], [3, 4]]))
print(res.numpy().tolist())
print([[1, 3], [2, 4]])
