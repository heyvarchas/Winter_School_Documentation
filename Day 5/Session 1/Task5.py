#Task: Implement Dijkstra’s Algorithm on the given graph.

graph = [['A', 'B', 4], ['A', 'C', 2], ['B', 'C', 1], ['B', 'D', 5], ['C', 'D', 8], ['D', 'E', 2], ['C', 'E', 10]]
# Define the graph as a list of edges: (source, destination, weight)

adj = {}
# Dictionary to store the adjacency list with weights

for u, v, w in graph:
    if u not in adj:
        adj[u] = []                   # Initialize adjacency list for node u
    adj[u].append((v, w))              # Add (neighbor, weight) to adjacency list

dist = {}
prev = {}
nodes = []
# dist: stores shortest distance from source to each node
# prev: stores previous node in the shortest path
# nodes: list of all unique nodes

for e in graph:
    dist[e[0]] = 9999                  # Initialize distance for source node
    dist[e[1]] = 9999                  # Initialize distance for destination node
    prev[e[0]] = None                  # Initialize previous node for source
    prev[e[1]] = None                  # Initialize previous node for destination
    if e[0] not in nodes:
        nodes.append(e[0])             # Add source node if not already present
    if e[1] not in nodes:
        nodes.append(e[1])             # Add destination node if not already present

dist['A'] = 0
# Set distance of the start node 'A' to 0

while nodes:                           # Dijkstra’s algorithm main loop
    u = nodes[0]
    for n in nodes:
        if dist[n] < dist[u]:
            u = n                      # Select node with minimum distance
    nodes.remove(u)                    # Remove the selected node from unvisited nodes

    if u in adj:
        for v, w in adj[u]:            # Relax edges from node u
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w  # Update shortest distance to v
                prev[v] = u            # Update previous node for v

path = []
cur = 'E'
# Reconstruct the shortest path from 'A' to 'E'

while cur:
    path.insert(0, cur)                # Insert current node at the beginning of the path
    cur = prev[cur]                    # Move to the previous node

print("Path:", path)                            # Print the shortest path from A to E
print("Distance:", dist['E'])                       # Print the total cost of the shortest path