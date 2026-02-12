def longest_word_from_file():
    filename = input("Enter filename: ")

    try:
        with open(filename, 'r') as file:
            words = file.read().split()
            if not words:
                print("File is empty!")
                return
            
            longest = max(words, key=len)
            print(f"Longest word: '{longest}' with {len(longest)} characters")

    except FileNotFoundError:
        print(f"File '{filename}' not found! ")

longest_word_from_file()