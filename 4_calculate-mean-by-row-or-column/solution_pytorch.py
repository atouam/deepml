import torch


def calculate_matrix_mean(matrix, mode: str) -> torch.Tensor:
    """
    Calculate mean of a 2D matrix per row or per column using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a 1-D tensor of means or raises ValueError on invalid mode.
    """
    a_t = torch.as_tensor(matrix, dtype=torch.float)
    if mode=="column":
        return torch.mean(a_t,0)
    elif mode=="row":
        return torch.mean(a_t,1)
    else:
        raise ValueError("Invalid mode. Use 'row' or 'column'.")


# Test Cases
# Test Case 1
print(calculate_matrix_mean([[1.0,2.0,3.0],[4.0,5.0,6.0]], 'column').numpy().tolist())
print([2.5, 3.5, 4.5])

# Test Case 2
print(calculate_matrix_mean([[1.0,2.0,3.0],[4.0,5.0,6.0]], 'row').numpy().tolist())
print([2.0, 5.0])

