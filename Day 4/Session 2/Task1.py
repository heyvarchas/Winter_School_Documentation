#Task: Write a program to implement Gradient Descent on a Simple Dataset for Logistic Regression.

import numpy as np                      # Import NumPy for numerical array operations
import math                             # Import math module for mathematical functions

X = np.array([1, 2, 3, 4, 5])            # Input feature array
y = np.array([1.5, 3.7, 3.2, 4.8, 6.1])  # Original target values (continuous)

y_bin = np.array([1 if v > 3 else 0 for v in y], dtype=float)
# Convert the target values into binary labels:
# 1 if value > 3, else 0 (binary classification)

w = 0.0                                 # Initialize weight
b = 0.0                                 # Initialize bias
lr = 0.1                                # Learning rate

for _ in range(1000):                   # Run gradient descent for 1000 iterations
    dw = 0.0                            # Gradient of loss w.r.t weight
    db = 0.0                            # Gradient of loss w.r.t bias

    for i in range(len(X)):             # Loop over each training sample
        z = w * X[i] + b                # Linear combination
        pred = 1 / (1 + math.exp(-z))   # Sigmoid activation (prediction)
        dw += (pred - y_bin[i]) * X[i]  # Accumulate gradient for weight
        db += (pred - y_bin[i])         # Accumulate gradient for bias

    w -= lr * dw / len(X)               # Update weight using average gradient
    b -= lr * db / len(X)               # Update bias using average gradient

print(round(w, 4), round(b, 4))
# Print the trained weight and bias rounded to 4 decimal places

predictions = []                        # List to store predicted probabilities
for i in range(len(X)):
    z = w * X[i] + b                    # Linear combination for each input
    predictions.append(round(1 / (1 + math.exp(-z)), 4))
    # Compute and store sigmoid output rounded to 4 decimal places

print(predictions)                     # Print the predicted probabilities