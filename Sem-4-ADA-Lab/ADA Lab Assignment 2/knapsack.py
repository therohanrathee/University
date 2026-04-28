def fractional_knapsack(weights, values, capacity):
    items = list(zip(weights, values))
    
    # sort by value/weight ratio (highest first)
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    
    total_profit = 0
    
    for w, v in items:
        if capacity >= w:
            total_profit += v
            capacity -= w
        else:
            total_profit += (v/w) * capacity
            break
    
    return total_profit


weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print("Maximum Profit:", fractional_knapsack(weights, values, capacity))
