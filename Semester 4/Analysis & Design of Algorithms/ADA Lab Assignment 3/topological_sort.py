from collections import defaultdict

graph = defaultdict(list)

graph[0].append(2)
graph[0].append(3)
graph[1].append(3)
graph[1].append(4)
graph[2].append(5)
graph[3].append(5)

visited = set()
stack = []

def dfs(v):
    visited.add(v)
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(neighbor)
    stack.append(v)

for i in range(6):
    if i not in visited:
        dfs(i)

print("Topological Sort:", stack[::-1])
