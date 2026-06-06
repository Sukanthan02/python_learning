"""
Lesson 1.1: Data Preprocessing with NumPy and Pandas
-----------------------------------------------------
This script covers the essentials of manipulating data arrays, tabular data,
and preparing them for machine learning models.
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def demonstrate_numpy():
    print("=== 1. NumPy Basics ===")
    # Creating a 1D array
    arr_1d = np.array([1, 2, 3, 4, 5])
    print(f"1D Array: {arr_1d}, Shape: {arr_1d.shape}")
    
    # Creating a 2D array (matrix)
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"2D Matrix:\n{matrix}\nShape: {matrix.shape}")
    
    # Mathematical operations
    print(f"Matrix multiplied by 2:\n{matrix * 2}")
    print(f"Mean of matrix: {np.mean(matrix)}")
    print(f"Standard deviation: {np.std(matrix)}")
    
    # Creating arrays of zeros, ones, and random numbers
    zeros = np.zeros((2, 3))
    random_nums = np.random.rand(3, 3) # Uniform distribution [0, 1)
    print(f"Random 3x3 Matrix:\n{random_nums}\n")


def demonstrate_pandas():
    print("=== 2. Pandas DataFrames ===")
    # Creating a synthetic dataset representing employee records
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona'],
        'Age': [25, 30, np.nan, 35, 40, 28], # Charlie's age is missing
        'Salary': [50000, 60000, 75000, np.nan, 120000, 58000], # Diana's salary is missing
        'Department': ['IT', 'HR', 'IT', 'Marketing', 'Executive', 'HR'],
        'Experience': [2, 5, 8, 10, 15, 3]
    }
    
    # Initialize DataFrame
    df = pd.DataFrame(data)
    print("Initial DataFrame:")
    print(df)
    print("\nDataFrame Summary info:")
    print(df.info())
    
    # --- Handling Missing Data ---
    print("\n--- Preprocessing: Handling Missing Values ---")
    # Method A: Fill missing numerical values with the column median/mean
    df['Age'] = df['Age'].fillna(df['Age'].median())
    
    # Method B: Fill missing salary with mean salary of the respective department
    # First, let's just fill it with overall mean for simplicity
    df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
    print("DataFrame after handling missing values:")
    print(df)
    
    # --- Data Filtering & Querying ---
    print("\n--- Filtering: IT Department Employees ---")
    it_employees = df[df['Department'] == 'IT']
    print(it_employees)
    
    # --- Grouping and Aggregation ---
    print("\n--- Grouping: Average Salary by Department ---")
    avg_salary_dept = df.groupby('Department')['Salary'].mean()
    print(avg_salary_dept)
    
    # --- Feature Scaling ---
    print("\n--- Feature Scaling (Standardization & MinMax) ---")
    # Prepare features for scaling (Age, Experience, Salary)
    features = df[['Age', 'Salary', 'Experience']].values
    
    # Standardization (Mean = 0, Variance = 1)
    scaler_std = StandardScaler()
    scaled_std = scaler_std.fit_transform(features)
    print("Standardized Features (first 3 rows):\n", scaled_std[:3])
    
    # MinMax Scaling (scales values between 0 and 1)
    scaler_minmax = MinMaxScaler()
    scaled_minmax = scaler_minmax.fit_transform(features)
    print("MinMax Scaled Features (first 3 rows):\n", scaled_minmax[:3])


if __name__ == "__main__":
    demonstrate_numpy()
    demonstrate_pandas()
