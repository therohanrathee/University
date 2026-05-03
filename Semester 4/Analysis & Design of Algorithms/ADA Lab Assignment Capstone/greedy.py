parcels = [(90, 15), (70, 25), (110, 20)]
capacity = 60

parcels.sort(key=lambda x: x[0]/x[1], reverse=True)

total_value = 0

for v, w in parcels:
    if capacity >= w:
        total_value += v
        capacity -= w

print("Total Value:", total_value)