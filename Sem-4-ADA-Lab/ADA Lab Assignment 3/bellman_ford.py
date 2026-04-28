def bellman_ford(edges, V, source):
    dist = [float('inf')] * V
    dist[source] = 0
    
    for _ in range(V-1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    return dist

edges = [
    (0, 1, 5), (0, 2, 3), (1, 2, -2),
    (1, 3, 6), (2, 3, 4)
]

print("Distances:", bellman_ford(edges, 4, 0))
