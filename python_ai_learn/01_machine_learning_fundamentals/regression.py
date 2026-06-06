"""
Lesson 1.2: Regression with Scikit-Learn
-----------------------------------------
This script demonstrates how to construct, train, evaluate, and visualize a 
Linear Regression model predicting continuous values using synthetic data.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def run_regression_demo():
    print("=== Supervised Learning: Regression ===")
    
    # 1. Generate Synthetic Data
    # Let's simulate predicting house prices (in $100k) based on size (in 1000 sq ft)
    # Price = 2 * Size + 1.5 + noise
    np.random.seed(42)
    X = 2.5 * np.random.rand(100, 1) + 1.0  # Sizes between 1000 and 3500 sq ft
    noise = 0.5 * np.random.randn(100, 1)
    y = 2.0 * X + 1.5 + noise
    
    print(f"Dataset generated. X shape: {X.shape}, y shape: {y.shape}")
    
    # 2. Split Data into Training and Testing Sets
    # 80% training, 20% testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Train size: {X_train.shape[0]}, Test size: {X_test.shape[0]}")
    
    # 3. Initialize and Train the Model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Print learned parameters
    # Equation: y = mx + c (slope and intercept)
    print(f"Trained Slope (Coefficient): {model.coef_[0][0]:.4f}")
    print(f"Trained Intercept: {model.intercept_[0]:.4f}")
    
    # 4. Make Predictions
    y_pred = model.predict(X_test)
    
    # 5. Evaluate the Model
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    print("\n--- Evaluation Metrics ---")
    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
    print(f"R-squared Score (R2): {r2:.4f} (Indicates {(r2 * 100):.1f}% variance captured)")
    
    # 6. Plot the Results and Save Visual
    plt.figure(figsize=(8, 6))
    plt.scatter(X_train, y_train, color='blue', alpha=0.5, label='Training Data')
    plt.scatter(X_test, y_test, color='green', alpha=0.7, label='Testing Data')
    plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')
    
    plt.title('House Price Prediction vs House Size')
    plt.xlabel('House Size (1000s Sq Ft)')
    plt.ylabel('Price ($100k)')
    plt.legend()
    plt.grid(True)
    
    # Save the plot image
    plot_filename = 'regression_plot.png'
    plt.savefig(plot_filename)
    print(f"\nPlot visualized and saved as '{plot_filename}'")
    plt.close()

if __name__ == '__main__':
    run_regression_demo()
