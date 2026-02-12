def character_count():
    string = input("Enter a string: ")

    char_dict = {}
    for char in string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    print("Character counts:")

    for char,count in char_dict.items():
        print(f"{char}: {count}")
character_count()