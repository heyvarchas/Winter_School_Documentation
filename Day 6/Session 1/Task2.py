#Task: Implement RRT on the given maze.

import cv2                              # Import OpenCV for image processing and display
import numpy as np                      # Import NumPy for numerical and array operations
import random                           # Import random module for random sampling

img = cv2.imread(r"maze.png")
# Read the maze image from the specified file path

img = cv2.resize(img, (400, 400))
# Resize the image to 400x400 pixels

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Convert the image to grayscale

_, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# Convert the grayscale image to a binary image (free space = white, obstacles = black)

start = (30, 370)                       # Define the start point
goal = (200, 395)                       # Define the goal point

nodes = [start]                        # Initialize the tree with the start node
parent = {start: None}                 # Dictionary to store parent of each node
step = 20                              # Step size for RRT expansion

def free(p):
    # Check whether a point lies in free space
    return bw[p[1], p[0]] == 255

def dist(a, b):
    # Compute Euclidean distance between two points
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5

def steer(a, b):
    # Steer from point a towards point b with maximum step size
    d = dist(a, b)
    if d < step:
        return b
    x = int(a[0] + step * (b[0]-a[0]) / d)
    y = int(a[1] + step * (b[1]-a[1]) / d)
    return (x, y)

def collision(a, b):
    # Check for collision along the straight line between a and b
    for i in range(21):
        x = int(a[0] + (b[0]-a[0]) * i / 20)
        y = int(a[1] + (b[1]-a[1]) * i / 20)
        if bw[y, x] == 0:
            return True
    return False

found = False                          # Flag to indicate whether a path to the goal is found

for _ in range(5000):                  # Run RRT expansion for a fixed number of iterations
    rand = (random.randint(0, 399), random.randint(0, 399))
    # Sample a random point in the image

    if not free(rand):
        continue                       # Skip if the sampled point is not in free space

    near = nodes[0]                    # Find the nearest existing node
    for n in nodes:
        if dist(n, rand) < dist(near, rand):
            near = n

    new = steer(near, rand)            # Generate a new node in the direction of the random point

    if free(new) and not collision(near, new):
        nodes.append(new)              # Add the new node to the tree
        parent[new] = near             # Store its parent

        if dist(new, goal) < step and not collision(new, goal):
            parent[goal] = new         # Connect the goal if it is reachable
            found = True
            break

if found:
    cur = goal                         # Backtrack from goal to start
    while parent[cur] is not None:
        p = parent[cur]
        cv2.line(img, p, cur, (0, 0, 255), 2)
        # Draw the path segment in red
        cur = p

cv2.imshow("RRT Path", img)            # Display the maze with the RRT path
cv2.waitKey(0)                         # Wait indefinitely until a key is pressed
cv2.destroyAllWindows()                # Close all OpenCV windows