import torch


def matrix_dot_vector(a, b) -> torch.Tensor:
    """
    Compute the product of matrix `a` and vector `b` using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a 1-D tensor of length m, or tensor(-1) if dimensions mismatch.
    """
    a_t = torch.as_tensor(a, dtype=torch.float)
    b_t = torch.as_tensor(b, dtype=torch.float)
    # Dimension mismatch check
    if a_t.size(1) != b_t.size(0):
        return torch.tensor(-1)
    # Your implementation here
    return a @ b


# Test Cases
# Test Case 1
res = matrix_dot_vector(
    torch.tensor([[1, 2, 3], [2, 4, 5], [6, 8, 9]], dtype=torch.float),
    torch.tensor([1, 2, 3], dtype=torch.float),
)
print(res.numpy().tolist())
print([14.0, 25.0, 49.0])

# Test Case 2
res = matrix_dot_vector(
    torch.tensor([[1, 2, 3], [2, 4, 5]], dtype=torch.float),
    torch.tensor([1, 2], dtype=torch.float),
)
print(res.numpy().tolist())
print(-1)
