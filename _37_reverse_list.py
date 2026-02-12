def reverse_list():
    def reverse(lst):
        reverse = lst[::-1]
        return reverse

    nums_str = input("Enter numbers separted by space: ").split()
    numbers = []
    for num in nums_str:
        numbers.append(int(num))
    reversed_nums = reverse(numbers)

    print(f"Original list: {numbers}")
    print(f"Reversed list: {reversed_nums}")
reverse_list()