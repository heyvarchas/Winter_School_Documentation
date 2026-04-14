#Task: Implement DFS Algorithm on the given graph.

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

visited = []
# List to keep track of visited nodes during DFS

def dfs(node):
    visited.append(node)              # Mark the current node as visited
    print(node)                       # Print the current node

    if node in adj:
        for n in adj[node]:           # Traverse all neighbors of the current node
            if n not in visited:
                dfs(n)                # Recursively visit unvisited neighbors

dfs('A')                              # Start DFS traversal from node 'A'
print(adj)                            # Print the adjacency list