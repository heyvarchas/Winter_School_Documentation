#Task: Take an image, convert it to black and white and detect the edges using Canny Edge Detection. 
#Pick two points and implement A* Algorithm to find the optimal path between the points. 
#Consider the edges to be obstacles.

import cv2                              # Import OpenCV for image processing and display
import numpy as np                      # Import NumPy for numerical and array operations

img = cv2.imread(r"maze_Astar.png")
# Read the maze image from the specified file path

img = cv2.resize(img, (400, 400))
# Resize the image to a fixed size of 400x400 pixels

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Convert the image to grayscale

edges = cv2.Canny(gray, 50, 150)
# Detect edges using the Canny edge detector

ys, xs = np.where(edges > 0)
# Get coordinates of edge pixels (obstacles)

min_x, max_x = xs.min(), xs.max()
min_y, max_y = ys.min(), ys.max()
# Determine the bounding box of the detected edges

mask = np.ones_like(edges) * 255
# Create a white mask image

mask[min_y:max_y, min_x:max_x] = edges[min_y:max_y, min_x:max_x]
# Keep edges only inside the bounding box and block everything else

edges = mask
# Update edges image with masked result

grid = edges / 255
# Convert edges image into a grid (0 = free, 1 = obstacle)

start = (30, 30)                        # Define the start position
end = (380, 380)                        # Define the end position

open_list = [(0, start)]                # Open list containing (f_score, node)
came_from = {}                          # Dictionary to reconstruct the path
g_score = {start: 0}                    # Cost from start to each node

while open_list:                        # Continue until there are nodes to explore
    open_list.sort()                    # Sort nodes by lowest f-score
    current = open_list.pop(0)[1]       # Select the node with the lowest f-score

    if current == end:
        break                           # Exit loop if the goal is reached

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        # Explore 4-connected neighbors (up, down, right, left)

        neighbor = (current[0] + dx, current[1] + dy)

        if 0 <= neighbor[0] < 400 and 0 <= neighbor[1] < 400:
            # Check if neighbor is within image boundaries

            if grid[neighbor[1], neighbor[0]] == 1:
                continue                # Skip if neighbor is an obstacle

            temp_g = g_score[current] + 1
            # Tentative cost from start to neighbor

            if neighbor not in g_score or temp_g < g_score[neighbor]:
                # Update path if a shorter one is found
                g_score[neighbor] = temp_g

                h = abs(neighbor[0] - end[0]) + abs(neighbor[1] - end[1])
                # Manhattan distance heuristic

                f_score = temp_g + h
                # Total estimated cost

                open_list.append((f_score, neighbor))
                came_from[neighbor] = current
                # Record the path

curr = end
while curr in came_from:
    img[curr[1], curr[0]] = [0, 0, 255]
    # Draw the final path in red on the original image
    curr = came_from[curr]

cv2.imshow('Edges', edges)
# Display the processed edge map with blocked regions

cv2.imshow('Path', img)
# Display the maze image with the A* path drawn

cv2.waitKey(0)                         # Wait indefinitely until a key is pressed
cv2.destroyAllWindows()                # Close all OpenCV windows