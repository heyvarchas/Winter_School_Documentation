#Task: Implement RRT* on the given maze.

import cv2                              # Import OpenCV for image processing and display
import numpy as np                      # Import NumPy for numerical operations
import random                           # Import random module for random sampling
import math                             # Import math module for mathematical functions

img = cv2.imread(r"maze.png")
# Read the maze image from the specified file path

img = cv2.resize(img, (400, 400))
# Resize the image to 400x400 pixels

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Convert the image to grayscale

_, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# Convert the grayscale image into a binary image (free space = white, obstacles = black)

start = (30, 370)                       # Define the start point
goal = (200, 395)                       # Define the goal point

nodes = [start]                        # Initialize the node list with the start node
parent = {start: None}                 # Dictionary to store parent relationships
cost = {start: 0}                      # Dictionary to store cost from start to each node

step = 20                              # Step size for tree expansion
radius = 40                            # Neighborhood radius for rewiring (RRT*)

def free(p):
    # Check if a point is within bounds and lies in free space
    return 0 <= p[0] < 400 and 0 <= p[1] < 400 and bw[p[1], p[0]] == 255

def dist(a, b):
    # Compute Euclidean distance between two points
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def steer(a, b):
    # Move from point a towards point b by at most 'step' distance
    d = dist(a, b)
    if d < step:
        return b
    x = int(a[0] + step * (b[0]-a[0]) / d)
    y = int(a[1] + step * (b[1]-a[1]) / d)
    return (x, y)

def collision(a, b):
    # Check whether the straight path from a to b intersects any obstacle
    for i in range(21):
        x = int(a[0] + (b[0]-a[0]) * i / 20)
        y = int(a[1] + (b[1]-a[1]) * i / 20)
        if bw[y, x] == 0:
            return True
    return False

for _ in range(6000):                  # Run the RRT* algorithm for a fixed number of iterations
    rand = (random.randint(0, 399), random.randint(0, 399))
    # Randomly sample a point in the image

    if not free(rand):
        continue                       # Skip if the sampled point is not in free space

    nearest = nodes[0]                 # Find the nearest existing node
    for n in nodes:
        if dist(n, rand) < dist(nearest, rand):
            nearest = n

    new = steer(nearest, rand)         # Generate a new node towards the random sample

    if not free(new) or collision(nearest, new):
        continue                       # Skip if new node is invalid or path is blocked

    best_parent = nearest
    best_cost = cost[nearest] + dist(nearest, new)
    # Initialize best parent and cost

    for n in nodes:
        if dist(n, new) < radius and not collision(n, new):
            c = cost[n] + dist(n, new)
            if c < best_cost:
                best_cost = c
                best_parent = n
    # Choose the best parent within the neighborhood (RRT* optimization)

    nodes.append(new)                  # Add the new node to the tree
    parent[new] = best_parent          # Assign its parent
    cost[new] = best_cost              # Store its cost

    for n in nodes:
        if n != new and dist(n, new) < radius and not collision(new, n):
            if cost[new] + dist(new, n) < cost[n]:
                parent[n] = new
                cost[n] = cost[new] + dist(new, n)
    # Rewire nearby nodes if a cheaper path is found

    if dist(new, goal) < step and not collision(new, goal):
        parent[goal] = new             # Connect the goal if reachable
        cost[goal] = cost[new] + dist(new, goal)
        break

cur = goal                             # Backtrack from goal to start
while cur in parent and parent[cur] is not None:
    p = parent[cur]
    cv2.line(img, p, cur, (0, 0, 255), 2)
    # Draw the path segment in red
    cur = p

cv2.imshow("RRT* Path", img)           # Display the maze with the RRT* path
cv2.waitKey(0)                         # Wait indefinitely until a key is pressed
cv2.destroyAllWindows()                # Close all OpenCV windows