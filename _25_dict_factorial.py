def factorial_dictionary():
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n-1)

    fact_dict = {}
    for i in range(1,16):
        fact_dict[i] = factorial(i)

    print("Dictionary with factorials:")
    for key,value in fact_dict.items():
        print(f"{key}! = {value}")

factorial_dictionary()