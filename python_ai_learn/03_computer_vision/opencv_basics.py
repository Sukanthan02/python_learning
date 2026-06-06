"""
Lesson 3.1: OpenCV Basics
--------------------------
This script demonstrates the basics of reading, writing, and transforming 
images using OpenCV. To ensure it runs out-of-the-box, we generate a synthetic 
image, save it, and then apply image processing techniques on it.
"""

import cv2
import numpy as np

def create_synthetic_image(filename="synthetic_shapes.png"):
    # Create a blank black image (400x400 pixels, 3 color channels: BGR)
    img = np.zeros((400, 400, 3), dtype=np.uint8)
    
    # Draw a blue rectangle (Start coord, End coord, BGR color, Thickness)
    # BGR format: Blue is (255, 0, 0)
    cv2.rectangle(img, (50, 50), (150, 150), (255, 0, 0), -1) # -1 thickness means fill
    
    # Draw a green circle (Center, Radius, BGR color, Thickness)
    # BGR format: Green is (0, 255, 0)
    cv2.circle(img, (270, 100), 60, (0, 255, 0), 3)
    
    # Draw a red line
    # BGR format: Red is (0, 0, 255)
    cv2.line(img, (50, 300), (350, 300), (0, 0, 255), 5)
    
    # Write some white text
    cv2.putText(img, "OpenCV Demo", (100, 230), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
    
    # Save image
    cv2.imwrite(filename, img)
    print(f"1. Created and saved synthetic image: {filename}")
    return filename


def process_image(img_path):
    print("\n--- Processing Image ---")
    # 1. Read the image
    # Note: OpenCV loads images in BGR order
    img = cv2.imread(img_path)
    if img is None:
        print("Error: Could not read image.")
        return
        
    print(f"Loaded Image shape: {img.shape} (Height, Width, Channels)")
    print(f"Data type: {img.dtype}")
    
    # 2. Convert to Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("cv_grayscale.png", gray)
    print("2. Converted image to grayscale and saved as 'cv_grayscale.png'")
    
    # 3. Resize the Image
    # Half the width and height
    height, width = img.shape[:2]
    resized = cv2.resize(img, (width // 2, height // 2))
    cv2.imwrite("cv_resized.png", resized)
    print(f"3. Resized image from {width}x{height} to {width//2}x{height//2} and saved as 'cv_resized.png'")
    
    # 4. Blur the Image (Gaussian Blur)
    # Kernel size must be positive and odd: (5, 5)
    blurred = cv2.GaussianBlur(img, (7, 7), 0)
    cv2.imwrite("cv_blurred.png", blurred)
    print("4. Applied Gaussian Blur and saved as 'cv_blurred.png'")
    
    # 5. Canny Edge Detection
    # Detects high intensity changes in the image
    # Thresholds: 100 (minVal) and 200 (maxVal)
    edges = cv2.Canny(gray, 100, 200)
    cv2.imwrite("cv_edges.png", edges)
    print("5. Applied Canny Edge Detection and saved as 'cv_edges.png'")


if __name__ == "__main__":
    path = create_synthetic_image()
    process_image(path)
