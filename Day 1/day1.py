def calculate_sum(lines):
    total_sum = 0
    for line in lines:
        digits = [char for char in line if char.isdigit()]
        if len(digits) >= 1:
            first_digit = digits[0]
            last_digit = digits[-1]
            calibration_value = first_digit + last_digit
            total_sum += int(calibration_value)
    return total_sum

if __name__ == "__main__":
    file_name = input("Enter the name of the text file: ")
    try:
        with open(file_name, 'r') as file:
            input_lines = file.readlines()
            result = calculate_sum(input_lines)
            print("Sum of values:", result)
    except FileNotFoundError:
        print("File not found.")
