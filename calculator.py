def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return "Unsupported operation"

if __name__ == "__main__":
    print("Result:", calculate(10, 5, '*'))
