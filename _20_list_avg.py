def list_average():
    n = int(input("How many elements? "))
    numbers = []

    for i in range(n):
        num = float(input(f"Enter element {i+1}: "))
        numbers.append(num)

    average = sum(numbers) / len(numbers)
    print(f"List: {numbers}")
    print(f"Average: {average:.2f}")

list_average()