import math
import cmath

def quadratic_roots():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    if a == 0:
        print("Not a quadratic equation!")
        return
    discriminant = (b**2) - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant) / (2*a))
        root2 = (-b - math.sqrt(discriminant) / (2*a))

    elif discriminant == 0:
        root = -b / (2*a)
        print(f"One real root: {root:.2f}")

    else:
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        print(f"Two complex roots: {root1} and {root2}")

quadratic_roots()

