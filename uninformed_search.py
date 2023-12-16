graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(graph, start, visited):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def dfid(graph, start, depth, visited=None):
    if visited is None:
        visited = set()
    if depth > 0:
        visited.add(start)
        print(start, end=' ')
        for neighbor in graph[start]:
            if neighbor not in visited:
                dfid(graph, neighbor, depth - 1, visited)

def bfs(graph, start):
    visited = set()
    queue = []
    queue.append(start)
    visited.add(start)
    while queue:
        node = queue.pop(0)
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("\nBFS traversal:")
bfs(graph, 'A')
print("\nDFID traversal:")
dfid(graph, 'A', 2)
print("\nDFS traversal:")
dfs(graph, 'A',None)
