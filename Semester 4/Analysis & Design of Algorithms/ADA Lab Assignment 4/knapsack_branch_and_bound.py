class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def bound(level, profit, weight, items, W):
    if weight >= W:
        return 0
    
    bound_profit = profit
    j = level + 1
    total_weight = weight
    
    while j < len(items) and total_weight + items[j].weight <= W:
        total_weight += items[j].weight
        bound_profit += items[j].value
        j += 1
    
    if j < len(items):
        bound_profit += (W - total_weight) * items[j].value / items[j].weight
    
    return bound_profit

def knapsack_bb(items, W):
    items.sort(key=lambda x: x.value/x.weight, reverse=True)
    
    max_profit = 0
    
    def solve(level, profit, weight):
        nonlocal max_profit
        
        if weight <= W and profit > max_profit:
            max_profit = profit
        
        if level+1 < len(items):
            if bound(level, profit, weight, items, W) > max_profit:
                solve(level+1,
                      profit + items[level+1].value,
                      weight + items[level+1].weight)
                
                solve(level+1, profit, weight)
    
    solve(-1, 0, 0)
    return max_profit

items = [Item(1,20), Item(4,70), Item(6,120)]
print("Max Profit:", knapsack_bb(items, 7))