#Task: Write a program to multiply two matrices of different dimensions.

import numpy as np   # Import NumPy for matrix and numerical operations

x = int(input("What is the number of rows in your first matrix? "))       # Number of rows in first matrix
y = int(input("What is the number of columns in your first matrix? "))    # Number of columns in first matrix
z = int(input("What is the number of columns in your second matrix? "))   # Number of columns in second matrix

m = np.full((x, y), 0, dtype=int)   # Initialize first matrix with zeros (size x × y)
n = np.full((y, z), 0, dtype=int)   # Initialize second matrix with zeros (size y × z)

for i in range(x):                  # Loop over rows of the first matrix
    for j in range(y):              # Loop over columns of the first matrix
        m[i][j] = int(input("Enter element (Matrix 1): "))  # Take input for first matrix elements

for i in range(y):                  # Loop over rows of the second matrix
    for j in range(z):              # Loop over columns of the second matrix
        n[i][j] = int(input("Enter element (Matrix 2): "))  # Take input for second matrix elements

final = np.full((x, z), 0, dtype=int)  # Initialize the result matrix with zeros (size x × z)

def multiply(a, b):                   # Function to multiply two matrices a and b
    for i in range(x):                # Loop over rows of the result matrix
        for j in range(z):            # Loop over columns of the result matrix
            for k in range(y):        # Loop for matrix multiplication logic
                final[i, j] = final[i, j] + a[i, k] * b[k, j]  # Accumulate the product
    print(final)                      # Print the final multiplied matrix

multiply(m, n)                        # Call the function to multiply matrices m and n