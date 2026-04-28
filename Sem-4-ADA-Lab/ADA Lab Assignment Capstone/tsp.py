import itertools

graph = [
    [0, 12, 18, 22],
    [12, 0, 25, 17],
    [18, 25, 0, 28],
    [22, 17, 28, 0]
]

n = len(graph)

min_cost = float('inf')

for perm in itertools.permutations(range(1, n)):
    cost = 0
    k = 0
    
    for j in perm:
        cost += graph[k][j]
        k = j
    
    cost += graph[k][0]
    min_cost = min(min_cost, cost)

print("Optimal Cost:", min_cost)