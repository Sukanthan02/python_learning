"""
Lesson 2.2: Building a Neural Network with PyTorch
----------------------------------------------------
This script builds a Multi-Layer Perceptron (MLP) to solve a non-linear 
classification problem (concentric circles). It highlights the use of 
non-linear activations (ReLU) and standard neural network training structures.
"""

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

# 1. Create a Non-Linear Dataset (Concentric Circles)
X, y = make_circles(n_samples=1000, noise=0.03, random_state=42, factor=0.8)

# Convert to PyTorch Tensors
X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.float32).unsqueeze(1) # Shape should match prediction shape (N, 1)

# Split into Train and Test sets
X_train, X_test, y_train, y_test = train_test_split(
    X_tensor, y_tensor, test_size=0.2, random_state=42
)

# 2. Define the Neural Network Architecture
class CircleClassifier(nn.Module):
    def __init__(self):
        super(CircleClassifier, self).__init__()
        # Layers definition
        self.network = nn.Sequential(
            nn.Linear(in_features=2, out_features=16), # Input layer -> Hidden Layer 1
            nn.ReLU(),                                 # Activation 1
            nn.Linear(in_features=16, out_features=8), # Hidden Layer 1 -> Hidden Layer 2
            nn.ReLU(),                                 # Activation 2
            nn.Linear(in_features=8, out_features=1),  # Hidden Layer 2 -> Output Layer
            nn.Sigmoid()                               # Output Activation (for Binary Probability)
        )
        
    def forward(self, x):
        return self.network(x)

# Initialize Model, Loss Function, and Optimizer
model = CircleClassifier()
print("--- Neural Network Architecture ---")
print(model)

# Binary Cross Entropy Loss is suitable for binary classification
criterion = nn.BCELoss() 
# Adam Optimizer dynamically scales the learning rate
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 3. Train the Neural Network
epochs = 400
print("\nTraining Neural Network...")

for epoch in range(1, epochs + 1):
    # Step A: Put model in training mode
    model.train()
    
    # Step B: Forward Pass
    predictions = model(X_train)
    
    # Step C: Compute Loss
    loss = criterion(predictions, y_train)
    
    # Step D: Reset accumulated gradients
    optimizer.zero_grad()
    
    # Step E: Backward Pass (Compute derivatives)
    loss.backward()
    
    # Step F: Update weights
    optimizer.step()
    
    # Track performance
    if epoch % 50 == 0 or epoch == 1:
        # Calculate training accuracy
        # predictions >= 0.5 becomes class 1, otherwise class 0
        predicted_classes = (predictions >= 0.5).float()
        correct = (predicted_classes == y_train).sum().item()
        accuracy = correct / len(y_train)
        
        print(f"Epoch {epoch:03d}/{epochs} | Loss: {loss.item():.4f} | Training Accuracy: {accuracy*100:.2f}%")

# 4. Evaluate on Unseen Test Data
model.eval() # Put model in evaluation mode (turns off dropout, batchnorm, etc.)
with torch.no_grad(): # Disable gradient computation to save memory and compute speed
    test_predictions = model(X_test)
    test_loss = criterion(test_predictions, y_test)
    test_classes = (test_predictions >= 0.5).float()
    test_correct = (test_classes == y_test).sum().item()
    test_accuracy = test_correct / len(y_test)

print("\n--- Test Set Evaluation ---")
print(f"Test Loss:     {test_loss.item():.4f}")
print(f"Test Accuracy: {test_accuracy*100:.2f}%")

# 5. Visualizing the Decision Boundary and Saving Plot
def plot_decision_boundary(model, X, y):
    # Setup coordinates grid
    x_min, x_max = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1
    y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    
    # Combine mesh points to pass to the model
    grid_points = np.c_[xx.ravel(), yy.ravel()]
    grid_tensor = torch.tensor(grid_points, dtype=torch.float32)
    
    # Predict probabilities for each grid point
    model.eval()
    with torch.no_grad():
        preds = model(grid_tensor).reshape(xx.shape).numpy()
    
    # Plotting contour and points
    plt.contourf(xx, yy, preds, cmap=plt.cm.RdYlBu, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdYlBu, edgecolors='k')
    plt.title("Neural Network Classification Boundary")
    plt.savefig("nn_decision_boundary.png")
    print("\nDecision boundary plot saved as 'nn_decision_boundary.png'")
    plt.close()

# Convert back to numpy for visualization
plot_decision_boundary(model, X_tensor.numpy(), y_tensor.numpy().squeeze())
