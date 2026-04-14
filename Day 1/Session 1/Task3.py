#Task: Slice a 4x4 2D array and make it 3x3, containing elements of the bottom right 9 elements.

import numpy as np                     # Import NumPy library for numerical operations

x = np.array([[0, 0, 0, 0],             # Create a 2D NumPy array (matrix)
              [0, 1, 2, 3],
              [0, 4, 5, 6],
              [0, 7, 8, 9]])

y = x[1:, 1:]                           # Slice the array: remove first row and first column
print(y)                                # Print the resulting submatrix