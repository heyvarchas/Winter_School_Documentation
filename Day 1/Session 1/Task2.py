#Task: Write a program to find nth element in Fibonacci Sequence

j = int(input("Which element of the Fibonacci Sequence do you want?"))  # Take user input for which Fibonacci element is required

list1 = [0 for p in range(j)]  # Create a list of size j initialized with 0s

list1[0] = 1                  # Set the first Fibonacci number to 1
list1[1] = 1                  # Set the second Fibonacci number to 1

for i in range(2, j):         # Loop from the third element up to the j-th element
    list1[i] = list1[i-1] + list1[i-2]  # Each Fibonacci number is the sum of the previous two

print(list1[j-1])             # Print the j-th Fibonacci number (0-based indexing)