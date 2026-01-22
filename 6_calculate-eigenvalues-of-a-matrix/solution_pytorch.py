import torch


def calculate_eigenvalues(matrix: torch.Tensor) -> torch.Tensor:
    """
    Compute eigenvalues of a 2×2 matrix using PyTorch.
    Input: 2×2 tensor; Output: 1-D tensor with the two eigenvalues in ascending order.
    """
    return torch.linalg.eigvals(matrix).real.sort().values


# Test Cases
# Test Case 1
res = calculate_eigenvalues(torch.tensor([[2.0, 0.0], [0.0, 3.0]]))
print(res.detach().numpy().tolist())
print([2.0, 3.0])

# Test Case 2
res = calculate_eigenvalues(torch.tensor([[0.0, 1.0], [1.0, 0.0]]))
print(res.detach().numpy().tolist())
print([-1.0, 1.0])

# Test Case 3
res = calculate_eigenvalues(torch.tensor([[4.0, 2.0], [1.0, 3.0]]))
print(res.detach().numpy().tolist())
print([2.0, 5.0])
