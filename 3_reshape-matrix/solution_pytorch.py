import torch


def reshape_matrix(a, new_shape) -> torch.Tensor:
    """
    Reshape a 2D matrix `a` to shape `new_shape` using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a tensor of shape `new_shape`, or an empty tensor on mismatch.
    """
    # Dimension check
    if len(a) * len(a[0]) != new_shape[0] * new_shape[1]:
        return torch.tensor([])
    # Convert to tensor and reshape
    a_t = torch.as_tensor(a, dtype=torch.float)
    return a_t.reshape(new_shape)

# Test Cases
# Test Case 1
res = reshape_matrix(
    torch.tensor([[1,2,3],[4,5,6]], dtype=torch.float),
    (3, 2)
)
print(res.numpy().tolist())
print([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])

# Test Case 2
res = reshape_matrix(
    torch.tensor([[1,2],[3,4]], dtype=torch.float),
    (3, 2)
)
print(res.numpy().tolist())
print([])

