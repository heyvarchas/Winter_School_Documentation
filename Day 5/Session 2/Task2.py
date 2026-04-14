#Task: Write the general code for A* Algorithm (When diagonal movement is allowed)

grid = [
    [0,0,0,0,0],
    [1,1,0,1,0],
    [0,0,0,1,0],
    [0,1,1,0,0],
    [0,0,0,0,0]
]
# Define a 5x5 grid
# 0 represents free space, 1 represents obstacles

start = (0, 0)                         # Starting position (x, y)
goal = (4, 4)                          # Goal position (x, y)

open_list = [start]                    # List of nodes to be evaluated
came_from = {}                         # Dictionary to reconstruct the path
g = {start: 0}                         # Cost from start to each node
f = {start: abs(start[0]-goal[0]) + abs(start[1]-goal[1])}
# f-score = g-score + heuristic (Manhattan distance)

def neighbors(n):
    x, y = n                           # Current node coordinates
    res = []                           # List to store valid neighbors
    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
        # Allow movement in 8 directions (including diagonals)
        nx, ny = x+dx, y+dy            # Neighbor coordinates
        if 0 <= nx < 5 and 0 <= ny < 5 and grid[ny][nx] == 0:
            res.append((nx, ny))       # Add neighbor if inside grid and not blocked
    return res

while open_list:                       # Continue until there are nodes to explore
    cur = open_list[0]                 # Initialize current node
    for n in open_list:
        if f[n] < f[cur]:
            cur = n                    # Select node with the lowest f-score

    if cur == goal:
        break                          # Stop search if goal is reached

    open_list.remove(cur)              # Remove current node from open list

    for n in neighbors(cur):           # Explore all valid neighbors
        # Determine step cost: diagonal moves cost 1.4, straight moves cost 1
        if abs(n[0]-cur[0]) + abs(n[1]-cur[1]) == 2:
            step = 1.4
        else:
            step = 1

        temp = g[cur] + step           # Tentative cost to reach neighbor

        if n not in g or temp < g[n]:
            came_from[n] = cur         # Update best parent for neighbor
            g[n] = temp                # Update g-score
            f[n] = g[n] + abs(n[0]-goal[0]) + abs(n[1]-goal[1])
            # Update f-score using Manhattan heuristic

            if n not in open_list:
                open_list.append(n)    # Add neighbor to open list

path = []
cur = goal
dist = 0                               # Total path length

while cur in came_from:                # Reconstruct path from goal to start
    p = came_from[cur]

    # Accumulate distance based on move type
    if abs(p[0]-cur[0]) + abs(p[1]-cur[1]) == 2:
        dist += 1.4
    else:
        dist += 1

    path.insert(0, cur)                # Insert current node at the beginning of the path
    cur = p

path.insert(0, start)                  # Add the start node to the path

print("Path:", path)                   # Print the final path
print("Path Length:", dist)            # Print the total path length