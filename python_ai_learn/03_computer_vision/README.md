# Module 3: Computer Vision 👁️

This module introduces Computer Vision (CV)—the field of AI that enables computers to interpret and understand digital images and videos. We will cover basic image processing using **OpenCV** and building **Convolutional Neural Networks (CNNs)** in PyTorch.

---

## 💡 Core Concepts

### 1. OpenCV vs. Pillow
*   **OpenCV (`opencv-python`):** C++ based, highly optimized for real-time vision applications. **Note:** OpenCV loads images in **BGR** (Blue, Green, Red) format by default, whereas most other Python libraries use **RGB**.
*   **Pillow (`Pillow`):** Ideal for simple image manipulation (opening, cropping, resizing, saving) and integrations with deep learning data loaders.

### 2. Convolutional Neural Networks (CNNs)
Traditional Feed-Forward Neural Networks (MLPs) struggle with images because:
1.  **Too many parameters:** A $224 \times 224 \times 3$ image has $150,528$ input dimensions. Connecting this directly to a hidden layer leads to millions of weights, causing overfitting.
2.  **Loss of spatial features:** Flattening an image into a 1D vector ignores pixel adjacency and patterns.

CNNs solve this using three main types of layers:

```mermaid
graph LR
    Input[Input Image] --> Conv[Convolutional Layer]
    Conv --> Pool[Max Pooling Layer]
    Pool --> Flatten[Flatten Layer]
    Flatten --> FC[Fully Connected Layer]
    FC --> Output[Predictions]
    style Input fill:#f9f,stroke:#333
    style Conv fill:#bbf,stroke:#333
    style Pool fill:#bfb,stroke:#333
    style Flatten fill:#fbb,stroke:#333
    style FC fill:#dff,stroke:#333
```

*   **Convolutional Layer (Conv):** Passes a small sliding window matrix (filter/kernel) over the image to detect features like edges, corners, or textures.
*   **Pooling Layer (Max/Average Pool):** Reduces the spatial dimensions (width and height) of feature maps, lowering parameter counts and computational cost, and providing translation invariance.
*   **Fully Connected (FC) Layer:** Standard neural network layers at the end of the CNN to perform final classification based on features extracted by Conv/Pool layers.

---

## 🛠️ Python Implementation Files

1.  **`opencv_basics.py`**: Demonstrates image creation, resizing, color space conversions (BGR to Grayscale/RGB), Gaussian Blurring, and Canny Edge Detection.
2.  **`cnn_mnist.py`**: Designs and trains a PyTorch CNN model to recognize handwritten digits from the MNIST dataset. Includes convolutional, pooling, and dense layers.
