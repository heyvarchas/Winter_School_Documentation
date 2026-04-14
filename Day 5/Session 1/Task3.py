#Task: Write a general code to implement DFS algorithm

graph = {
    'A': [],
    'B': [],
    'C': [],
    'D': [],
    'E': [],
    'F': []
}

start = 'A'

visited = set()
stack = [start]

while stack:
    node = stack.pop()
    if node not in visited:
        print(node)
        visited.add(node)
        for n in reversed(graph[node]):
            if n not in visited:
                stack.append(n)