#Task: Write the general code for A* Algorithm (When diagonal movement is not allowed)

grid = [
    [0,0,0,0,0],
    [1,1,0,1,0],
    [0,0,0,1,0],
    [0,1,1,0,0],
    [0,0,0,0,0]
]
# Define the grid map
# 0 represents free space, 1 represents obstacles

start = (0, 0)                         # Starting position (x, y)
goal = (4, 4)                          # Goal position (x, y)

open_list = [start]                    # List of nodes to be explored
came_from = {}                         # Dictionary to reconstruct the path
g = {start: 0}                         # Cost from start to each node
f = {start: abs(start[0]-goal[0]) + abs(start[1]-goal[1])}
# f-score = g-score + heuristic (Manhattan distance)

def neighbors(n):
    x, y = n                           # Current node coordinates
    res = []                           # List to store valid neighbors
    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx, ny = x+dx, y+dy            # Compute neighbor coordinates
        if 0 <= nx < 5 and 0 <= ny < 5 and grid[ny][nx] == 0:
            res.append((nx, ny))       # Add neighbor if inside grid and not an obstacle
    return res

while open_list:                       # Continue until there are nodes to explore
    cur = open_list[0]                 # Initialize current node
    for n in open_list:
        if f[n] < f[cur]:
            cur = n                    # Select node with lowest f-score

    if cur == goal:
        break                          # Stop search when goal is reached

    open_list.remove(cur)              # Remove current node from open list

    for n in neighbors(cur):           # Explore all valid neighbors
        temp = g[cur] + 1              # Tentative g-score for neighbor
        if n not in g or temp < g[n]:
            came_from[n] = cur         # Record best path to neighbor
            g[n] = temp                # Update g-score
            f[n] = g[n] + abs(n[0]-goal[0]) + abs(n[1]-goal[1])
            # Update f-score using Manhattan heuristic

            if n not in open_list:
                open_list.append(n)    # Add neighbor to open list if not present

path = []
cur = goal                             # Start path reconstruction from goal
while cur in came_from:
    path.insert(0, cur)                # Insert node at the beginning of the path
    cur = came_from[cur]
path.insert(0, start)                  # Add the start node to the path

dist = len(path) - 1                   # Compute path length (number of steps)

print("Path:", path)                   # Print the final path
print("Path Length:", dist)            # Print the length of the path