def largest_without_builtin():
    n = int(input("How many elements? "))

    if n <= 0:
        print("List is empty!")
        return
    
    largest = float(input("Enter element 1: "))

    for i in range(1,n):
        num = float(input(f"Enter element {i+1}: "))
        if num > largest:
            largest = num
        print(f"Largest number: {largest}")

largest_without_builtin()