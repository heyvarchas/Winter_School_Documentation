import cv2
import numpy as np
import random
import math

# Load and resize
img = cv2.imread("maze.png")
img_bnw = cv2.imread("maze_bnw.png")
if img is None or img_bnw is None:
    print("Error: Could not load maze.png")
    exit()

ht, wt = 785, 1264

img = cv2.resize(img, (wt, ht))
img_bnw = cv2.resize(img_bnw, (wt, ht))
img_copy = img.copy() # Keep a clean copy for drawing the final path

# --- Point Selection Section ---
lst = []
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN and len(lst) < 2:
        # Check if the clicked point is actually white (free space)
        if bw[y, x] == 255:
            print(f"Point {len(lst)+1} Captured! X: {x}, Y: {y}")
            lst.append((x, y))
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow("Select Points", img)
        else:
            print("Warning: You clicked an obstacle! Try again.")

gray = cv2.cvtColor(img_bnw, cv2.COLOR_BGR2GRAY)
_, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((3,3), np.uint8) 
bw = cv2.dilate(bw, kernel, iterations=1)

cv2.imshow("Select Points", img)
cv2.setMouseCallback("Select Points", click_event)

print("1. Click START point (white space) | 2. Click GOAL point (white space)")
while len(lst) < 2:
    cv2.waitKey(1)

cv2.destroyWindow("Select Points")

# --- RRT* Setup ---
start = lst[0]
goal = lst[1]
nodes = [start]
parent = {start: None}
cost = {start: 0}

step = 20
radius = 40
path_found = False

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def steer(a, b):
    d = dist(a, b)
    if d < step:
        return b
    x = int(a[0] + step * (b[0]-a[0]) / d)
    y = int(a[1] + step * (b[1]-a[1]) / d)
    return (x, y)

def collision(a, b):
    for i in range(21):
        x = int(a[0] + (b[0]-a[0]) * i / 20)
        y = int(a[1] + (b[1]-a[1]) * i / 20)
        # Boundary conditions
        if x < 0 or x >= wt or y < 0 or y >= ht or bw[y, x] == 0:
            return True
    return False

# --- Main Iterations ---
print("Searching for path...")
for i in range(20000):
    # 10% Goal Bias to help it find the target faster
    if random.random() < 0.10:
        rand = goal
    else:
        rand = (random.randint(0, wt - 1), random.randint(0, ht - 1))
    
    # Standard RRT finding nearest
    nearest = min(nodes, key=lambda n: dist(n, rand))
    new = steer(nearest, rand)

    if 0 <= new[0] < wt and 0 <= new[1] < ht:
        if bw[new[1], new[0]] == 255 and not collision(nearest, new):
            
            # RRT* Optimization: Find best parent
            best_parent = nearest
            best_cost = cost[nearest] + dist(nearest, new)
            
            for n in nodes:
                if dist(n, new) < radius and not collision(n, new):
                    c = cost[n] + dist(n, new)
                    if c < best_cost:
                        best_cost = c
                        best_parent = n
            
            nodes.append(new)
            parent[new] = best_parent
            cost[new] = best_cost

            # RRT* Rewiring
            for n in nodes:
                if n != new and dist(n, new) < radius and not collision(new, n):
                    if cost[new] + dist(new, n) < cost[n]:
                        parent[n] = new
                        cost[n] = cost[new] + dist(new, n)

            # Check if goal reached
            if dist(new, goal) < step and not collision(new, goal):
                parent[goal] = new
                cost[goal] = cost[new] + dist(new, goal)
                path_found = True
                print(f"Goal reached in {i} iterations!")
                break

# --- Path Visualization ---
if path_found:
    cur = goal
    while cur in parent and parent[cur] is not None:
        p = parent[cur]
        cv2.line(img_copy, p, cur, (0, 0, 255), 2)
        cv2.imshow("RRT* Final Path", img_copy)
        cv2.waitKey(50) # Faster feedback
        cur = p
    print("Path rendering complete.")
else:
    print("No path found within iteration limit.")

cv2.waitKey(0)
cv2.destroyAllWindows()