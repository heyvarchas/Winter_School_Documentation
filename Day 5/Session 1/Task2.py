#Task: Implement BFS Algorithm on the given graph.

graph = [['A', 'B', 4], ['A', 'C', 2], ['B', 'C', 1], ['B', 'D', 5], ['C', 'D', 8], ['D', 'E', 2], ['C', 'E', 10]]
# Define the graph as a list of edges with weights (u, v, weight)

adj = {}
# Initialize an empty adjacency list dictionary

for e in graph:
    u = e[0]                          # Source node of the edge
    v = e[1]                          # Destination node of the edge
    if u not in adj:
        adj[u] = []                   # Create a list for the node if it doesn't exist
    adj[u].append(v)                  # Add the neighbor to the adjacency list

start = 'A'
# Define the starting node for BFS

visited = []
queue = []
# Initialize visited list and queue for BFS traversal

visited.append(start)                 # Mark the start node as visited
queue.append(start)                   # Add the start node to the queue

while queue:
    node = queue.pop(0)               # Remove the first element from the queue (FIFO)
    print("Popped:", node)             # Print the node being processed

    if node in adj:
        for n in adj[node]:            # Traverse all neighbors of the current node
            if n not in visited:
                visited.append(n)     # Mark neighbor as visited
                queue.append(n)       # Add neighbor to the queue

print(visited)                        # Print the order of visited nodes
print(adj)                            # Print the adjacency list