def calc():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Operator (+,-,*,/): ")

    if op == '+': print(a + b)
    elif op == '-': print(a - b)
    elif op == '*': print(a * b)
    elif op == '/': print(a / b)

calc()