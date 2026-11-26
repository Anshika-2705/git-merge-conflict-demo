def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '/':
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Error: unknown operator"

if __name__ == "__main__":
    print("Result:", calculate(10, 5, '/'))
