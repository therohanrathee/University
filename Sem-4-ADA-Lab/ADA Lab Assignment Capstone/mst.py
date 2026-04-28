import heapq

graph = {
    0: [(5,1), (7,2)],
    1: [(5,0), (9,3), (6,4)],
    2: [(7,0), (8,4)],
    3: [(9,1), (4,4)],
    4: [(6,1), (8,2), (4,3)]
}

def prim(start):
    visited = set()
    heap = [(0, start)]
    cost = 0
    
    while heap:
        w, node = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            cost += w
            for wt, nbr in graph[node]:
                heapq.heappush(heap, (wt, nbr))
    
    return cost

print("MST Cost:", prim(0))