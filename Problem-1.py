class Calculator:
    def __init__(math, a: float, b: float, operation: str):
        math.a = a
        math.b = b
        math.operation = operation.lower()

    def calculate(math):
        if math.operation == "add":
            return math.a + math.b

        elif math.operation == "sub":
            return math.a - math.b

        elif math.operation == "mul":
            return math.a * math.b

        elif math.operation == "div":
            if math.b == 0:
                return "Error: Division by zero is not allowed."
            return math.a / math.b

        else:
            return "Invalid operation! Use add, sub, mul, or div."


a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
op = input("Enter operation (add / sub / mul / div): ")

calc = Calculator(a, b, op)
result = calc.calculate()
print("Result:", result)
