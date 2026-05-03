graph = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]

def tsp_recursive(pos, visited):
    if visited == (1<<len(graph)) - 1:
        return graph[pos][0]
    
    ans = sys.maxsize
    
    for city in range(len(graph)):
        if visited & (1<<city) == 0:
            new_ans = graph[pos][city] + tsp_recursive(city, visited | (1<<city))
            ans = min(ans, new_ans)
    
    return ans

print("Minimum Cost:", tsp_recursive(0,1)) 
