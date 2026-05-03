# Adjacency List
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1],
    3: [0, 2]
}

print("Adjacency List:", graph)

# Adjacency Matrix
matrix = [
    [0,1,0,1],
    [1,0,1,0],
    [0,1,0,0],
    [1,0,1,0]
]

print("Adjacency Matrix:")
for row in matrix:
    print(row)
