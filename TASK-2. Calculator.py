def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by zero"
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

try:
    num1 = float(input("What's the first number?: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation: ")
if operation_symbol not in operations:
    print("Invalid operation.")
    exit()

try:
    num2 = float(input("What's the next number?: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

calculation_function = operations[operation_symbol]
Result = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {Result}")
