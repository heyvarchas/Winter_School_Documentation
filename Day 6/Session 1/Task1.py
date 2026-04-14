#Task: Implement PRM on the given maze.

import cv2                              # Import OpenCV for image processing and display
import numpy as np                      # Import NumPy for numerical and array operations
import random                           # Import random module for random sampling

img = cv2.imread(r"maze.png")
# Read the maze image from the specified file path

img = cv2.resize(img, (400, 400))
# Resize the image to 400x400 pixels

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Convert the image to grayscale

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# Apply binary thresholding to obtain a free-space (white) and obstacle (black) map

start = (30, 370)                       # Define the start node coordinates
end = (200, 395)                        # Define the end node coordinates
nodes = [start, end]                   # Initialize node list with start and end nodes

while len(nodes) < 100:                # Randomly sample nodes until total nodes = 100
    rx = random.randint(5, 395)        # Random x-coordinate within bounds
    ry = random.randint(5, 395)        # Random y-coordinate within bounds
    if thresh[ry, rx] == 255:
        nodes.append((rx, ry))          # Add node only if it lies in free space

adj = {i: [] for i in range(len(nodes))}
# Create an adjacency list for each node

for i in range(len(nodes)):             # Loop over all node pairs
    for j in range(i + 1, len(nodes)):
        p1 = nodes[i]
        p2 = nodes[j]

        dist = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
        # Compute Euclidean distance between two nodes

        if dist < 100:
            # Consider connecting nodes only if within a distance threshold

            line_img = np.zeros((400, 400), dtype=np.uint8)
            # Create a blank image to test collision along the edge

            cv2.line(line_img, p1, p2, 255, 1)
            # Draw a line between the two nodes

            if not np.any(cv2.bitwise_and(line_img, cv2.bitwise_not(thresh))):
                # Check if the line intersects any obstacle
                adj[i].append(j)        # Add edge i -> j
                adj[j].append(i)        # Add edge j -> i (undirected graph)

queue = [(0, [0])]                      # Priority queue storing (distance, path)
visited = set()                         # Set to track visited nodes
path = []                               # Final path storage

while queue:                            # Dijkstra-style search through the roadmap
    queue.sort()                        # Sort queue by distance
    dist, current_path = queue.pop(0)  # Extract the shortest path so far
    last_node = current_path[-1]        # Get the last node in the path
    
    if last_node == 1:
        path = current_path             # Path found to the end node
        break
        
    if last_node not in visited:
        visited.add(last_node)          # Mark node as visited
        for neighbor in adj[last_node]:
            # Explore all connected neighbors
            new_dist = dist + (
                (nodes[last_node][0]-nodes[neighbor][0])**2 +
                (nodes[last_node][1]-nodes[neighbor][1])**2
            )**0.5
            # Update distance with edge cost

            queue.append((new_dist, current_path + [neighbor]))
            # Push new path to the queue

for i in range(len(path)-1):
    cv2.line(img, nodes[path[i]], nodes[path[i+1]], (0, 0, 255), 2)
    # Draw the final path on the maze image in red

cv2.imshow('PRM Path', img)             # Display the maze with PRM path
cv2.waitKey(0)                          # Wait indefinitely until a key is pressed
cv2.destroyAllWindows()                 # Close all OpenCV windows