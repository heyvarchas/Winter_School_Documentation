#Task: Write a program to run Fibonacci Series

i = 1            # Initialize variable i with value 1
j = 1            # Initialize variable j with value 1

print(i)         # Print the initial value of i
print(j)         # Print the initial value of j

for k in range(1, 6):   # Loop runs 5 times with k taking values from 1 to 5
    m = j              # Store the current value of j in temporary variable m
    j = j + i          # Update j to be the sum of j and i
    i = m              # Update i to the old value of j (stored in m)
    print(j)           # Print the updated value of j