#Task: Write a general code to implement BFS algorithm

graph = {
    'A': [],
    'B': [],
    'C': [],
    'D': [],
    'E': [],
    'F': []
}
# Define a graph using an adjacency list representation
# Each key is a node, and the value is a list of connected neighbors

start = 'A'
# Define the starting node for BFS traversal

visited = set()
# Set to keep track of visited nodes

queue = [start]
# Initialize the queue with the starting node

while queue:                            # Continue traversal while the queue is not empty
    node = queue.pop(0)                 # Remove the first element from the queue (FIFO)

    if node not in visited:
        print(node)                     # Print the current node
        visited.add(node)               # Mark the node as visited

        for n in graph[node]:           # Iterate over all neighbors of the current node
            if n not in visited:
                queue.append(n)         # Add unvisited neighbors to the queue