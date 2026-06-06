"""
Lesson 1.3: Classification with Scikit-Learn
---------------------------------------------
This script demonstrates how to train a Random Forest Classifier to diagnose 
breast cancer (malignant or benign) based on cellular features, then 
evaluate its performance using accuracy, precision, recall, and a confusion matrix.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

def run_classification_demo():
    print("=== Supervised Learning: Classification ===")
    
    # 1. Load Dataset
    cancer_data = load_breast_cancer()
    X = cancer_data.data
    y = cancer_data.target
    feature_names = cancer_data.feature_names
    target_names = cancer_data.target_names # ['malignant', 'benign']
    
    print(f"Dataset Loaded: Breast Cancer Diagnostics")
    print(f"Features shape: {X.shape} (Features: {len(feature_names)})")
    print(f"Classes: {target_names} (0 = Malignant, 1 = Benign)")
    
    # 2. Split Data
    # 75% training, 25% testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    print(f"Training set size: {X_train.shape[0]}, Testing set size: {X_test.shape[0]}")
    
    # 3. Train Classifier (Random Forest)
    print("\nTraining Random Forest Classifier...")
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    # 4. Predict
    y_pred = clf.predict(X_test)
    
    # 5. Evaluate
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    print("\n--- Key Metrics ---")
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}  (Out of predicted Benign, how many were actually Benign)")
    print(f"Recall:    {recall:.4f}     (Out of actual Benign, how many did we successfully find)")
    print(f"F1-Score:  {f1:.4f}")
    
    # Classification Report
    print("\n--- Detailed Classification Report ---")
    print(classification_report(y_test, y_pred, target_names=target_names))
    
    # Confusion Matrix
    # Format: 
    # [ [True Negatives, False Positives],
    #   [False Negatives, True Positives] ]
    print("--- Confusion Matrix ---")
    cm = confusion_matrix(y_test, y_pred)
    print(f"True Malignant (TN): {cm[0][0]} | False Benign (FP): {cm[0][1]}")
    print(f"False Malignant (FN): {cm[1][0]} | True Benign (TP): {cm[1][1]}")
    
    # Print feature importance for educational value
    print("\n--- Top 5 Most Important Features ---")
    importances = clf.feature_importances_
    sorted_indices = importances.argsort()[::-1]
    for i in range(5):
        index = sorted_indices[i]
        print(f"{i+1}. {feature_names[index]}: {importances[index]:.4f}")

if __name__ == '__main__':
    run_classification_demo()
