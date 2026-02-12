def file_statistics():
    filename = input("Enter file name: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            lines = content.split('\n')

            char_count = len(content)
            word_count = len(content.split())
            line_count = len(lines)

            print(f"Statistics for '{filename}':")
            print(f"Characters: {char_count}")
            print(f"Words: {word_count}")
            print(f"Lines: {line_count}")

    except FileNotFoundError:
        print(f"Filne '{filename}' not found!")

file_statistics()