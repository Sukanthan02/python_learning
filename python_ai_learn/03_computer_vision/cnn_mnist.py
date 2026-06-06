"""
Lesson 3.2: Convolutional Neural Networks (CNN) with PyTorch
--------------------------------------------------------------
This script constructs a custom dataset of 28x28 grayscale images containing 
either circles (Class 0) or vertical lines (Class 1). It then designs a CNN 
using Conv2d, MaxPool2d, and Linear layers, training it to classify the shapes.
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np

# 1. Create a Synthetic Shapes Dataset
class ShapesDataset(Dataset):
    def __init__(self, num_samples=1000):
        self.num_samples = num_samples
        self.data = []
        self.labels = []
        
        for _ in range(num_samples):
            # Start with blank canvas (28x28 grayscale)
            img = np.zeros((28, 28), dtype=np.float32)
            
            # Randomly select shape: 0 = circle, 1 = vertical line
            label = np.random.choice([0, 1])
            
            if label == 0:
                # Draw a simulated circle (a ring of high pixels)
                center_x, center_y = np.random.randint(10, 18, size=2)
                radius = np.random.randint(5, 8)
                for theta in np.linspace(0, 2 * np.pi, 30):
                    x = int(center_x + radius * np.cos(theta))
                    y = int(center_y + radius * np.sin(theta))
                    if 0 <= x < 28 and 0 <= y < 28:
                        img[y, x] = 1.0
            else:
                # Draw a vertical line
                col = np.random.randint(10, 18)
                start_row = np.random.randint(3, 8)
                end_row = np.random.randint(20, 25)
                img[start_row:end_row, col] = 1.0
            
            # Add Gaussian noise
            img += np.random.normal(0.0, 0.1, img.shape).astype(np.float32)
            img = np.clip(img, 0.0, 1.0)
            
            # PyTorch expects (Channel, Height, Width) format for images
            # Adding channel dimension: (1, 28, 28)
            img = np.expand_dims(img, axis=0)
            
            self.data.append(img)
            self.labels.append(label)
            
        self.data = torch.tensor(np.array(self.data), dtype=torch.float32)
        self.labels = torch.tensor(self.labels, dtype=torch.long)
        
    def __len__(self):
        return self.num_samples
        
    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

# 2. Design the CNN Architecture
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        
        # Convolutional Block 1
        # Input: (1, 28, 28) -> Output: (8, 28, 28)
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=8, kernel_size=3, stride=1, padding=1)
        self.relu1 = nn.ReLU()
        # MaxPool Input: (8, 28, 28) -> Output: (8, 14, 14)
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        # Convolutional Block 2
        # Input: (8, 14, 14) -> Output: (16, 14, 14)
        self.conv2 = nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.relu2 = nn.ReLU()
        # MaxPool Input: (16, 14, 14) -> Output: (16, 7, 7)
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        # Fully Connected (Dense) Layers
        # 16 channels * 7 height * 7 width = 784 inputs
        self.fc1 = nn.Linear(16 * 7 * 7, 64)
        self.relu3 = nn.ReLU()
        self.fc2 = nn.Linear(64, 2) # 2 Output classes (Circle or Line)
        
    def forward(self, x):
        # Pass through Conv Block 1
        x = self.pool1(self.relu1(self.conv1(x)))
        # Pass through Conv Block 2
        x = self.pool2(self.relu2(self.conv2(x)))
        
        # Flatten the features map into a 1D vector
        x = x.view(-1, 16 * 7 * 7)
        
        # Pass through dense layers
        x = self.relu3(self.fc1(x))
        x = self.fc2(x)
        return x

def train_cnn():
    # Setup data loaders
    train_dataset = ShapesDataset(num_samples=800)
    test_dataset = ShapesDataset(num_samples=200)
    
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)
    
    # Initialize network, optimizer, and loss
    model = SimpleCNN()
    print("--- CNN Network Structure ---")
    print(model)
    
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.005)
    
    # Training loop
    epochs = 10
    print("\nTraining CNN...")
    
    for epoch in range(1, epochs + 1):
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0
        
        for images, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item() * images.size(0)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            
        epoch_loss = running_loss / total
        epoch_acc = (correct / total) * 100
        print(f"Epoch {epoch:02d}/{epochs} | Loss: {epoch_loss:.4f} | Training Accuracy: {epoch_acc:.2f}%")
        
    # Evaluate on Test Data
    model.eval()
    test_correct = 0
    test_total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            test_total += labels.size(0)
            test_correct += (predicted == labels).sum().item()
            
    test_acc = (test_correct / test_total) * 100
    print("\n--- Test Set Evaluation ---")
    print(f"Test Accuracy: {test_acc:.2f}%")

if __name__ == "__main__":
    train_cnn()
