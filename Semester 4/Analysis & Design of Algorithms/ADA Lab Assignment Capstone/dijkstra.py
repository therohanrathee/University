import heapq

graph = {
    0: [(1, 7), (2, 9), (3, 14)],
    1: [(0, 7), (2, 10), (4, 15)],
    2: [(0, 9), (1, 10), (3, 11)],
    3: [(0, 14), (2, 11), (4, 6)],
    4: [(1, 15), (3, 6)]
}

def dijkstra(start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    
    pq = [(0, start)]
    
    while pq:
        d, node = heapq.heappop(pq)
        
        for neighbor, weight in graph[node]:
            if d + weight < dist[neighbor]:
                dist[neighbor] = d + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))
    
    return dist

print(dijkstra(0))