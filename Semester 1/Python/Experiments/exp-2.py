a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
operator = input("Choose Operator (+,-,/,*,%,//) : ")

# Performing the required operation based on the operator entered by the user

if operator == '+' :
    print(f"{a} + {b} = {a+b}")

elif operator == '-' :
    print(f"{a} - {b} = {a-b}")

elif operator == '*' :
    print(f"{a} * {b} = {a*b}")

elif operator == '/' :
    print(f"{a} / {b} = {a/b}")

elif operator=='%' :
    print(f"{a} % {b} = {a%b}")

elif operator == '//' :
    print(f"{a} // {b} = {a//b}")
    
else :
    print("Error")