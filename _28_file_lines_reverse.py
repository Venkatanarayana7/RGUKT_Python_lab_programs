def reverse_file_lines():
    filename = input("Enter filename: ")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            print("Lines in reverse order: ")
            for line in reversed(lines):
                print(line.rstrip())

    except FileNotFoundError:
        print(f"File '{filename}' not found!")

reverse_file_lines()