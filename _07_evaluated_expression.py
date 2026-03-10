def evaluate_expression():
    a = float(input("Enter value of a: "))
    b = float(input("Enter value of b: "))
    x = float(input("Enter value of x: "))

    if (a*x - b) == 0:
        print("Division by zero erro!")
    else:
        result = (a*x + b) / (a*x - b)
        print(f"Results: {result:.2f}")

evaluate_expression()