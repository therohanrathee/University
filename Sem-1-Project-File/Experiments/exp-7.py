def bitwise_operation(arr1, arr2, operator) :


    if len(arr1) != len(arr2) :
        raise ValueError("Arrays must have the same length")
    
    if operator == "AND" :
        return [a & b for a, b in zip(arr1, arr2)]
    
    elif operator == "OR" :
        return [a | b for a, b in zip(arr1, arr2)]
    
    elif operator == "XOR" :
        return [a ^ b for a, b in zip(arr1, arr2)]
    
    else :
        raise ValueError("Invalid operator. Use 'AND', 'OR', or 'XOR'.")
    
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

print(bitwise_operation(arr1, arr2, "AND"))
print(bitwise_operation(arr1, arr2, "OR"))
print(bitwise_operation(arr1, arr2, "XOR"))