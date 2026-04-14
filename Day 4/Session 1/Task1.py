#Task: Write a program to implement Gradient Descent on a Simple Dataset and find the best fit line

import numpy as np                      # Import NumPy for numerical computations
import matplotlib.pyplot as plt         # Import Matplotlib for plotting graphs

X = np.array([1, 2, 3, 4, 5])            # Input feature array (e.g., hours studied)
y = np.array([1.5, 3.7, 3.2, 4.8, 6.1])  # Target values (e.g., exam scores)

m = 0.0                                 # Initialize slope (weight) of the linear model
b = 0.0                                 # Initialize intercept (bias) of the linear model
lr = 0.01                               # Learning rate for gradient descent
epochs = 100                            # Number of training iterations

for i in range(epochs):                # Loop for gradient descent optimization
    y_pred = m * X + b                 # Predict values using the current model
    error = y_pred - y                 # Compute prediction error
    
    dm = (2/len(X)) * np.dot(error, X) # Gradient of loss w.r.t slope (m)
    db = (2/len(X)) * np.sum(error)    # Gradient of loss w.r.t intercept (b)
    
    m -= lr * dm                       # Update slope using gradient descent
    b -= lr * db                       # Update intercept using gradient descent

print(f"\nFinal model: y = {m:.2f}x + {b:.2f}")
# Print the final learned linear equation

plt.scatter(X, y, color='blue', label="Actual data")
# Plot the actual data points

plt.plot(X, m * X + b, color='red', label="Fitted line")
# Plot the fitted regression line

plt.xlabel("Hours studied")             # Label the x-axis
plt.ylabel("Exam score")                # Label the y-axis
plt.legend()                            # Show legend
plt.show()                              # Display the plot