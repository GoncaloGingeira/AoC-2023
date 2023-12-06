import math
import numpy as np

def get_winning_times(t1, t2):
    x1 = math.floor((t1 - math.sqrt(t1 ** 2 - 4 * t2)) / 2) + 1
    x2 = math.ceil((t1 + math.sqrt(t1 ** 2 - 4 * t2)) / 2) - 1
    return x2 - x1 + 1

def get_part1(input):
    return np.array([get_winning_times(x[0], x[1]) for x in input]).prod()

def get_part2(input):
    return get_winning_times(int(''.join([str(x[0]) for x in input])), int(''.join([str(x[1]) for x in input])))

if __name__ == "__main__":
    file_name = input("Enter the name of the text file: ")
    input = []
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            times = [int(x.strip()) for x in lines[0].split(" ") if x.strip().isnumeric()]
            distances = [int(x.strip()) for x in lines[1].split(" ") if x.strip().isnumeric()]
            for i in range(len(times)):
                input.append([times[i], distances[i]])

        print("Total ways part 1:", get_part1(input))
        print("Total ways part 2:", get_part2(input))
    except FileNotFoundError:
        print("File not found.")