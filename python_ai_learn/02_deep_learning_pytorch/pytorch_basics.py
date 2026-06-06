"""
Lesson 2.1: PyTorch Tensors and Autograd Basics
-----------------------------------------------
This script covers the fundamentals of working with PyTorch tensors (the main 
building blocks of neural networks) and demonstrates automatic differentiation.
"""

import torch
import numpy as np

def tensor_basics():
    print("=== 1. Creating Tensors ===")
    # Creating a tensor from a list
    t_list = torch.tensor([1.0, 2.0, 3.0])
    print(f"Tensor from list: {t_list}, dtype: {t_list.dtype}")
    
    # Creating a random tensor of a specific shape (e.g. 2 rows, 3 cols)
    t_rand = torch.randn(2, 3)
    print(f"Random Normal Tensor:\n{t_rand}")
    
    # Converting NumPy array to PyTorch Tensor
    np_arr = np.array([[4, 5], [6, 7]])
    t_np = torch.from_numpy(np_arr)
    print(f"\nTensor from NumPy:\n{t_np}")
    
    # Converting back to NumPy
    print("Back to NumPy array:", t_np.numpy())


def tensor_operations():
    print("\n=== 2. Tensor Math Operations ===")
    x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
    y = torch.tensor([[5.0, 6.0], [7.0, 8.0]])
    
    # Element-wise operations
    print(f"Element-wise addition:\n{x + y}")
    print(f"Element-wise multiplication:\n{x * y}")
    
    # Matrix Multiplication (Dot product)
    # Equivalent to x @ y or torch.matmul(x, y)
    matrix_product = torch.matmul(x, y)
    print(f"Matrix Multiplication:\n{matrix_product}")


def device_management():
    print("\n=== 3. Hardware Acceleration (CUDA/GPU) ===")
    # Check if a GPU is available
    cuda_available = torch.cuda.is_available()
    print(f"Is CUDA (NVIDIA GPU) available: {cuda_available}")
    
    # Select target device (GPU if available, else CPU)
    device = torch.device("cuda" if cuda_available else "cpu")
    print(f"Using device: {device}")
    
    # Move a tensor to the target device
    x = torch.randn(3, 3)
    x_device = x.to(device)
    print(f"Tensor moved to {x_device.device}")


def demonstrate_autograd():
    print("\n=== 4. Automatic Differentiation (Autograd) ===")
    # Let's say we want to compute the gradient of y = 3 * x^2 + 5 * x with respect to x at x = 2
    # Analytical derivative: dy/dx = 6 * x + 5
    # For x = 2: dy/dx = 6(2) + 5 = 17
    
    # We must explicitly tell PyTorch to track gradients for this variable
    x = torch.tensor(2.0, requires_grad=True)
    
    # Define our equation
    y = 3 * (x ** 2) + 5 * x
    print(f"Equation evaluated at x=2: y = {y.item()}")
    
    # Execute backpropagation (calculate derivatives)
    y.backward()
    
    # Access the calculated derivative (dy/dx)
    print(f"Calculated gradient dy/dx at x=2: {x.grad.item()} (Should be 17)")


if __name__ == "__main__":
    tensor_basics()
    tensor_operations()
    device_management()
    demonstrate_autograd()
