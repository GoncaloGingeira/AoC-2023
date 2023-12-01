import re

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

def calculate_sum_with_strings(lines):
    total_sum = 0
    for line in lines:
        newLine = replace_line(line)
        digits = [char for char in newLine if char.isdigit()]
        if len(digits) >= 1:
            first_digit = digits[0]
            last_digit = digits[-1]
            calibration_value = first_digit + last_digit
            total_sum += int(calibration_value)
                 
    return total_sum

def replace_line(line):
    replacements = [
        ("one", "o1e"), ("two", "t2o"), ("three", "t3e"), ("four", "f4r"),
        ("five", "f5e"), ("six", "s6x"), ("seven", "s7n"), ("eight", "e8t"),
        ("nine", "n9e")
    ]

    replacements.sort(key=lambda x: len(x[0]), reverse=True)

    pattern = "|".join([re.escape(old) for old, _ in replacements])
    replace_dict = {re.escape(old): new for old, new in replacements}
    regex = re.compile(pattern)

    def replace_func(match):
        return replace_dict[re.escape(match.group(0))]

    replaced_line = line
    while True:
        new_line = regex.sub(replace_func, replaced_line)
        if new_line == replaced_line:
            break
        replaced_line = new_line

    return replaced_line
    
    
if __name__ == "__main__":
    file_name = input("Enter the name of the text file: ")
    try:
        with open(file_name, 'r') as file:
            input_lines = file.readlines()
            result1 = calculate_sum(input_lines)
            print("Sum of values half 1:", result1)
            result2 = calculate_sum_with_strings(input_lines)
            print("Sum of values half 1:", result2)
    except FileNotFoundError:
        print("File not found.")
