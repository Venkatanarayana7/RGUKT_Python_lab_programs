# swap numbers without third variable
def swap_without_third():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Before swap: a = {a}, b = {b}")

    """
    a = 5
    b = 10
    a+= b  15
    b = a - b 5
    a = a-b  10

    """
    a += b
    b = a - b
    a -= b

    print(f"After swap: a = {a}, b = {b}")

swap_without_third()
