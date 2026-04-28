# Graph (Distance Matrix)
graph = [
    [0, 12, 18, 25],
    [12, 0, 30, 20],
    [18, 30, 0, 28],
    [25, 20, 28, 0]
]

# Parcels
parcels = [
    {"id": 1, "value": 80, "weight": 15},
    {"id": 2, "value": 50, "weight": 10},
    {"id": 3, "value": 120, "weight": 25}
]

# Vehicle Constraint
capacity = 50

print(graph)
print(parcels)