def digit_sum_to_file():
    input_file = input("Enter input filename: ")
    output_file = input("Enter output filename: ")

    def digit_sum(n):
        return sum(int(digit) for digit in str(n))
    
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                numbers = [int(num) for num in line.split() if num.isdigit()]

                for number in numbers:
                    dsum = digit_sum(number)
                    outfile.write(f"{number}: {dsum}\n")

        print(f"Digit sums written to {output_file}")
    except FileNotFoundError:
        print(f"Input file not found!")

digit_sum_to_file()