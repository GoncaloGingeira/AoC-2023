from collections import defaultdict

def get_nbrs(i, j1, j2):
    nbr_set = set()
    for j in range(j1, j2):
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if (di, dj) == (0, 0):
                    continue
                nbri, nbrj = i + di, j + dj
                if 0 <= nbri < n and 0 <= nbrj < m:
                    nbr_set.add((nbri, nbrj))
    return nbr_set

def is_char_symbol(char):
    return (not char.isdigit()) and char != '.'

def get_total_value(n, m):
    total = 0
    table = defaultdict(list)
    for i in range(n):
        j = 0
        while j < m:
            if not grid[i][j].isdigit():
                j += 1
                continue
            j2 = j + 1
            while j2 < m and grid[i][j2].isdigit():
                j2 += 1
            if any(is_char_symbol(grid[nbri][nbrj]) for nbri, nbrj in get_nbrs(i, j, j2)):
                num = int(grid[i][j:j2])
                total += num
                for nbri, nbrj in get_nbrs(i, j, j2):
                    if grid[nbri][nbrj] == '*':
                        table[(nbri, nbrj)].append(num)
            j = j2
    gear_sum = 0
    for v in table.values():
        if len(v) == 2:
            gear_sum += (v[0]*v[1])
    return total , gear_sum
    
if __name__ == "__main__":
    file_name = input("Enter the name of the text file: ")
    try:
        grid = []
        with open(file_name, 'r') as file:
            for line in file.readlines():
                grid.append(line.strip())
     
        n = len(grid)
        m = len(grid[0])
        
        total, gear_sum = get_total_value(n, m)
        print(total)
        print(gear_sum)

    except FileNotFoundError:
        print("File not found.")
        
        