import cv2
import numpy as np
import random
import math
from itertools import permutations

# --- Configuration ---
IMG_WIDTH = 1264
IMG_HEIGHT = 785
STEP_SIZE = 20
RADIUS = 40
MAX_ITER_SOLVE = 7000  # High iterations for the final path
MAX_ITER_COST = 3000   # Lower iterations just to estimate distance

# Load images and resize
img_color = cv2.imread("maze.png")
img_original = cv2.imread("maze_bnw.png")
if img_color is None or img_original is None:
    print("Error: maze.png not found.")
    exit()

img_display = cv2.resize(img_color, (IMG_WIDTH, IMG_HEIGHT))
img_display_bnw = cv2.resize(img_original, (IMG_WIDTH, IMG_HEIGHT))
gray = cv2.cvtColor(img_display_bnw, cv2.COLOR_BGR2GRAY)
_, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((3,3), np.uint8) 
bw = cv2.dilate(bw, kernel, iterations=1)

clicked_points = []

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        if bw[y, x] == 255:
            clicked_points.append((x, y))
            cv2.circle(img_display, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow("Select Points", img_display)
        else:
            print("Cannot place point on an obstacle!")

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def steer(a, b, step):
    d = dist(a, b)
    if d < step: return b
    return (int(a[0] + step * (b[0]-a[0]) / d), 
            int(a[1] + step * (b[1]-a[1]) / d))

def is_collision(a, b):
    for i in range(21):
        x = int(a[0] + (b[0]-a[0]) * i / 20)
        y = int(a[1] + (b[1]-a[1]) * i / 20)
        if x < 0 or x >= IMG_WIDTH or y < 0 or y >= IMG_HEIGHT or bw[y, x] == 0:
            return True
    return False

def get_path_cost(start, goal):
    """Calculates approximate real distance through the maze."""
    nodes = [start]
    cost = {start: 0}
    for _ in range(MAX_ITER_COST):
        rand = (random.randint(0, IMG_WIDTH-1), random.randint(0, IMG_HEIGHT-1))
        nearest = min(nodes, key=lambda n: dist(n, rand))
        new = steer(nearest, rand, STEP_SIZE)
        if 0 <= new[0] < IMG_WIDTH and 0 <= new[1] < IMG_HEIGHT:
            if bw[new[1], new[0]] == 255 and not is_collision(nearest, new):
                nodes.append(new)
                cost[new] = cost[nearest] + dist(nearest, new)
                if dist(new, goal) < STEP_SIZE and not is_collision(new, goal):
                    return cost[new] + dist(new, goal)
    return 999999 # Large no. for unreachable points

def solve_true_tsp(points):
    """Solves TSP using actual maze distances."""
    n = len(points)
    print("Calculating maze cost matrix (this may take a moment)...")
    cost_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            c = get_path_cost(points[i], points[j])
            cost_matrix[i][j] = cost_matrix[j][i] = c
    
    # Manual labour ughhh
    best_path = None
    min_total_cost = float('inf')
    
    # First point clicked is the start node
    for p in permutations(range(1, n)):
        current_path = [0] + list(p)
        current_cost = sum(cost_matrix[current_path[i]][current_path[i+1]] for i in range(n-1))
        if current_cost < min_total_cost:
            min_total_cost = current_cost
            best_path = current_path
            
    return [points[i] for i in best_path]

def run_rrt_star(start, goal):
    """Final high-quality path generation."""
    nodes = [start]
    parent = {start: None}
    cost = {start: 0}
    for _ in range(MAX_ITER_SOLVE):
        rand = (random.randint(0, IMG_WIDTH-1), random.randint(0, IMG_HEIGHT-1))
        nearest = min(nodes, key=lambda n: dist(n, rand))
        new = steer(nearest, rand, STEP_SIZE)
        if 0 <= new[0] < IMG_WIDTH and 0 <= new[1] < IMG_HEIGHT:
            if bw[new[1], new[0]] == 255 and not is_collision(nearest, new):
                best_parent, best_cost = nearest, cost[nearest] + dist(nearest, new)
                for n in nodes:
                    if dist(n, new) < RADIUS and not is_collision(n, new):
                        c = cost[n] + dist(n, new)
                        if c < best_cost: best_cost, best_parent = c, n
                nodes.append(new)
                parent[new], cost[new] = best_parent, best_cost
                for n in nodes:
                    if n != new and dist(n, new) < RADIUS and not is_collision(new, n):
                        if cost[new] + dist(new, n) < cost[n]:
                            parent[n], cost[n] = new, cost[new] + dist(new, n)
                if dist(new, goal) < STEP_SIZE and not is_collision(new, goal):
                    parent[goal] = new
                    return parent, goal
    return None, None

# --- End of Function Definitions ---
# --- Main Program ---
cv2.imshow("Select Points", img_display)
cv2.setMouseCallback("Select Points", click_event)
print("Click 4-8 points. Press any key to calculate TRUE shortest path.")
cv2.waitKey(0)
cv2.destroyWindow("Select Points")

if len(clicked_points) < 2: exit()

sorted_path = solve_true_tsp(clicked_points)
final_img = img_display.copy()

for i in range(len(sorted_path) - 1):
    p_start, p_goal = sorted_path[i], sorted_path[i+1]
    
    parent_map, last_node = run_rrt_star(p_start, p_goal)
    if last_node:
        curr = last_node
        while curr in parent_map and parent_map[curr] is not None:
            prev = parent_map[curr]
            cv2.line(final_img, prev, curr, (255, 0, 255), 2)
            curr = prev
        cv2.imshow("Final Optimized TSP Path", final_img)
        cv2.waitKey(100)

cv2.waitKey(0)
cv2.destroyAllWindows()