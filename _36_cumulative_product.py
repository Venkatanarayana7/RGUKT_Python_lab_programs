def cumulative_product():
    def product(lst):
        result = []
        product = 1

        for num in lst:
            product *=  num
            result.append(product)
            
        return result


    nums_str = input("Enter numbers separted by space: ").split()
    numbers = []
    for num in nums_str:
        numbers.append(float(num))
    cumulative = product(numbers)
    
    print(f"Original list: {numbers}")
    print(f"Cumulative product: {cumulative}")

cumulative_product()