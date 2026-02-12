def average_excluding_zeros():
    n = int(input("How many elements? "))
    numbers = []
    non_zero = []

    for i in range(n):
        num = float(input(f"Enter element {i+1}: "))
        numbers.append(num)

    for x in numbers:
        if x != 0:
            non_zero.append(x)
    if non_zero:
        average = sum(non_zero) / len(non_zero)
        print(f"List: {numbers}")
        print(f"Average excluding zeros: {average:.2f}")
    else:
        print("All elements are zero!")

average_excluding_zeros()