# Module 1: Machine Learning Fundamentals 📊

This module covers the foundations of classical machine learning using Python's core data science libraries: **NumPy**, **Pandas**, and **Scikit-Learn**.

---

## 💡 Core Concepts

### 1. The Machine Learning Pipeline
Before writing code, it is essential to understand the typical end-to-end ML lifecycle:
1.  **Data Collection:** Gathering raw numbers, text, images, or tabular data.
2.  **Data Preprocessing (Data Cleaning):** Handling missing values, scaling features, and encoding categorical variables.
3.  **Exploratory Data Analysis (EDA):** Visualizing patterns, correlation checks, and distribution plotting.
4.  **Feature Engineering:** Creating new variables or selecting relevant ones to improve performance.
5.  **Model Training:** Fitting a mathematical function to data.
6.  **Model Evaluation:** Scoring performance using indicators (e.g., accuracy, MSE) on unseen test data.
7.  **Inference (Deployment):** Using the trained model on real-world inputs.

### 2. Types of Machine Learning
*   **Supervised Learning:** The model is trained on labeled data (inputs and corresponding correct answers).
    *   *Regression:* Predicting a continuous numerical value (e.g., house prices).
    *   *Classification:* Predicting discrete labels (e.g., email spam detection).
*   **Unsupervised Learning:** The model finds patterns in unlabeled data.
    *   *Clustering:* Grouping similar objects together (e.g., customer segmentation).
    *   *Dimensionality Reduction:* Simplifying dataset dimensions while preserving variance (e.g., PCA).

---

## 🛠️ Python Implementation Files

In this folder, we have three fundamental scripts:

1.  **`data_processing.py`**: Covers Pandas and NumPy. Demonstrates creating arrays, reading data, handling missing values, scaling features, and prepping data.
2.  **`regression.py`**: Uses Scikit-Learn to fit a `LinearRegression` model. Explains Mean Squared Error (MSE) and R-squared ($R^2$) metrics.
3.  **`classification.py`**: Implements a `RandomForestClassifier` to determine cancer diagnostics. Illustrates precision, recall, F1-score, and confusion matrix reports.

---

## 📈 Evaluation Metrics Summary

### Regression Metrics
*   **Mean Squared Error (MSE):** The average squared difference between predictions and targets. Penalizes large errors heavily.
*   **Root Mean Squared Error (RMSE):** Standard deviation of the residuals ($\sqrt{MSE}$). Expressed in target units.
*   **R-squared ($R^2$):** Coefficient of determination. Measures the proportion of variance in the dependent variable predictable from the independent variables (closer to 1.0 is better).

### Classification Metrics
*   **Accuracy:** $\frac{True\ Positives\ +\ True\ Negatives}{Total\ Predictions}$. Simple but misleading on imbalanced datasets.
*   **Precision:** $\frac{True\ Positives}{True\ Positives\ +\ False\ Positives}$. Focuses on minimizing False Positives (e.g., don't mark good email as spam).
*   **Recall (Sensitivity):** $\frac{True\ Positives}{True\ Positives\ +\ False\ Negatives}$. Focuses on minimizing False Negatives (e.g., don't miss a cancerous tumor).
*   **F1-Score:** Harmonic mean of Precision and Recall. $2 \times \frac{Precision \times Recall}{Precision + Recall}$. Useful for balanced comparison.
