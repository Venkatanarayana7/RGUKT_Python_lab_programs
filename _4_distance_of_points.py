import math

def distance_between_points():
    x1 = float(input("Enter x-coordinate of point 1: "))
    y1 = float(input("Enter y-coordinate of point 1: "))
    x2 = float(input("Enter x-coordinate of point 2: "))
    y2 = float(input("Enter y-coordinate of point 2: "))

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 ) 
    print(f"Distance between points: {distance:.2f}")

distance_between_points()