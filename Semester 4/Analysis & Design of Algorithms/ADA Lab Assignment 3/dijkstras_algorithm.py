import heapq

graph = {
    0: [(1, 3), (2, 6)],
    1: [(2, 4), (3, 4)],
    2: [(3, 2)],
    3: [(4, 1)],
    4: []
}

def dijkstra(start):
    pq = [(0, start)]
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    
    while pq:
        d, node = heapq.heappop(pq)
        
        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return dist

print("Shortest Paths:", dijkstra(0))
