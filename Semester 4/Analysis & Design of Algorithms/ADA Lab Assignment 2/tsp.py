import itertools

def tsp(graph):
    n = len(graph)
    cities = list(range(1, n))
    
    min_cost = float('inf')
    
    for perm in itertools.permutations(cities):
        cost = 0
        k = 0
        
        for j in perm:
            cost += graph[k][j]
            k = j
        
        cost += graph[k][0]
        min_cost = min(min_cost, cost)
    
    return min_cost


graph = [
    [0, 10, 15],
    [10, 0, 20],
    [15, 20, 0]
]

print("Minimum Cost:", tsp(graph))
