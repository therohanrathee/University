def and_gate(a, b):
    return a and b

def or_gate(a, b):
    return a or b

def not_gate(a):
    return not a

def nand_gate(a, b):
    return not (a and b)

def nor_gate(a, b):
    return not (a or b)

def xor_gate(a, b):
    return a != b

# Test the gates
a = bool(int(input("Enter the first input : ")))
b = bool(int(input("Enter the second input : ")))
gate_type = input("Enter the gate type (AND, OR, NOT, NAND, NOR, XOR): ").upper()


if gate_type == 'AND' :
    result = and_gate(a, b)
elif gate_type == 'OR' :
    result = or_gate(a, b)

elif gate_type == 'NOT' :
    result = not_gate(a)
elif gate_type == 'NAND' :
    result = nand_gate(a, b)
elif gate_type == 'NOR' :
    result = nor_gate(a, b)
elif gate_type == 'XOR' :
    result = xor_gate(a, b)
else :
    print("Invalid gate type.")
    result = None

if result is not None :
    print(f"The result of {gate_type} operation is: {result}")