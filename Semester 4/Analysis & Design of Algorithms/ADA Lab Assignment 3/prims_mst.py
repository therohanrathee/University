import heapq

graph = {
    0: [(4,1), (3,2)],
    1: [(4,0), (2,2), (5,3)],
    2: [(3,0), (2,1), (7,3), (8,4)],
    3: [(5,1), (7,2), (6,4)],
    4: [(8,2), (6,3)]
}

def prim(start):
    visited = set()
    min_heap = [(0, start)]  # (weight, node)
    total_cost = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if node not in visited:
            visited.add(node)
            total_cost += weight

            for w, neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w, neighbor))

    return total_cost

print("Minimum Cost of MST:", prim(0))
