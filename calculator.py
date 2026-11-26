def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return "Invalid operator"

if __name__ == "__main__":
    print("Result:", calculate(10, 5, '+'))
