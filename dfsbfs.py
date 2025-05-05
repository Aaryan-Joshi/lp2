def dfs(graph, node, visited):
    if node not in visited:
        visited.add(node)
        print(node + " ", end="")
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)

def bfs(graph, node, visited, queue):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s + " ", end="")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Proper graph definition
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Initialize visited sets and queue
visited1 = set()
visited2 = set()
queue = []

# Run DFS and BFS
print("DFS:")
dfs(graph, 'A', visited1)

print("\nBFS:")
bfs(graph, 'A', visited2, queue)
