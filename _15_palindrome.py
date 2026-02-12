def is_number_palindrome():
    num = input("Enter a number: ")
    
    if num == num[::-1]:
        print(f"{num} is a palindrome")
    else:
        print(f"{num} is not a palindrome")

is_number_palindrome()