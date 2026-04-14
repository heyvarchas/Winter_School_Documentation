#Task: Write the code for linear regression using gradient descent method on the California Housing Dataset.

from sklearn.model_selection import train_test_split   # Import function to split data into training and test sets
import numpy as np                                     # Import NumPy for numerical computations
from numpy.linalg import inv                           # Import matrix inversion function

data = np.genfromtxt("housing.csv", delimiter=",", skip_header=1)
# Load the dataset from CSV, skipping the header row

X = data[:, :-1]
# Extract all columns except the last one as input features

y = data[:, -1]
# Extract the last column as the target variable

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2, random_state = 42
)
# Split the dataset into training (80%) and testing (20%) sets

class LinearRegressionGDloops:
    def __init__(self, learning_rate=0.01, iterations=1000):
      self.learning_rate = learning_rate
      self.iterations = iterations
      self.theta = None
      self.mse_history_train = []
      self.mse_history_val = []
      # Initialize learning rate, number of iterations, parameters,
      # and lists to store training and validation MSE history

    def fit(self, X_train, y_train, X_test, y_test):
      # Train the model using gradient descent
      # Add intercept term to X
      X_train_b = self.add_intercept(X_train)
      X_test_b = self.add_intercept(X_test)

      m, n = X_train_b.shape
      self.theta = np.zeros(n)
      # Initialize parameter vector (theta) with zeros

      # Gradient Descent loop
      for _ in range(self.iterations):
          predictions_train = self.predict(X_train_b)
          # Predict outputs for training data

          gradients = (2/m) * X_train_b.T.dot(predictions_train - y_train)
          # Compute gradients of the MSE loss w.r.t parameters

          self.theta -= self.learning_rate * gradients
          # Update parameters using gradient descent

          # Compute and store MSE for training set
          mse_train = self.compute_mse(y_train, predictions_train)
          self.mse_history_train.append(mse_train)

          # Compute and store MSE for validation (test) set
          predictions_test = self.predict(X_test_b)
          mse_test = self.compute_mse(y_test, predictions_test)
          self.mse_history_val.append(mse_test)

    def predict(self, X):
        # Predict output values using the learned parameters
        y_pred = []
        for i in range(X.shape[0]):
            y_pred.append(np.dot(X[i, :], self.theta))
        return np.array(y_pred)

    def compute_mse(self, y_true, y_pred):
        # Compute Mean Squared Error
        return np.mean((y_true - y_pred) ** 2)

    def add_intercept(self, X):
        # Add a column of ones to include the intercept (bias) term
        return np.c_[np.ones(X.shape[0]), X]

    # Helper method to retrieve MSE history for plotting
    def get_mse_history(self):
        return [self.mse_history_train, self.mse_history_val]

# Compute parameters using the normal equation (closed-form solution)
def normal_equation(X, y):
    X_b = np.c_[np.ones(X.shape[0]), X]
    # Add intercept term to feature matrix
    return inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
    # Solve the normal equation to get optimal parameters

# Create and train the gradient descent linear regression model
model = LinearRegressionGDloops(learning_rate=0.01, iterations=1000)
model.fit(X_train, y_train, X_test, y_test)
# Fit the model using training data and evaluate on test data