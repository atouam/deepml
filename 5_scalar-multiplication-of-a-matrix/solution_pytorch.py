import torch


def scalar_multiply(matrix, scalar) -> torch.Tensor:
    """
    Multiply each element of a 2D matrix by a scalar using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a 2D tensor of the same shape.
    """
    # Convert input to tensor
    m_t = torch.as_tensor(matrix, dtype=torch.float)
    return scalar * m_t


# Test Cases
# Test Case 1
res = scalar_multiply(torch.tensor([[1, 2], [3, 4]], dtype=torch.float), 3)
print(res.numpy().tolist())
print([[3.0, 6.0], [9.0, 12.0]])

# Test Case 2
res = scalar_multiply(torch.tensor([[1.5, 2.5], [3.0, 4.0]], dtype=torch.float), 2.0)
print(res.numpy().tolist())
print([[3.0, 5.0], [6.0, 8.0]])
