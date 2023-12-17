def dfs(graph, start, visited=None, goal=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(f"Visited: {visited}, Non-Visited: {set(graph.keys()) - visited}")
    print(start, end=' ')
    if start == goal:
        print(f"\nGoal state '{goal}' reached!")
        return
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, goal)

def dfid(graph, start, depth, visited=None, goal=None):
    if visited is None:
        visited = set()
    if depth > 0:
        visited.add(start)
        print(f"Visited: {visited}, Non-Visited: {set(graph.keys()) - visited}")
        print(start, end=' ')
        if start == goal:
            print(f"\nGoal state '{goal}' reached!")
            return
        for neighbor in graph[start]:
            if neighbor not in visited:
                dfid(graph, neighbor, depth - 1, visited, goal)

def bfs(graph, start, goal=None):
    visited = set()
    queue = []
    queue.append(start)
    visited.add(start)
    while queue:
        node = queue.pop(0)
        print(f"Visited: {visited}, Non-Visited: {set(graph.keys()) - visited}")
        print(node, end=' ')
        if node == goal:
            print(f"\nGoal state '{goal}' reached!")
            return
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# print("\nBFS traversal:")
# bfs(graph, 'A', 'C')
# print("\nDFID traversal:")
# dfid(graph, 'A', 2, goal='F')
print("\nDFS traversal:")
dfs(graph, 'A', goal='F')
