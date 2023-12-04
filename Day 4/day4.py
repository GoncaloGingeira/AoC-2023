if __name__ == "__main__":
    file_name = input("Enter the name of the text file: ")

    try:
        with open(file_name, 'r') as file:
             matches = [len(set(line[:40].split()) & set(line[42:].split())) for line in file.readlines()]

        cards = [1] * len(matches)
        for i, n in enumerate(matches):
            for j in range(n):
                cards[i + j + 1] += cards[i]

        print("Total cards is: ",sum(2 ** (n - 1) for n in matches if n > 0))
        print("Sum of cards: ", sum(cards))

    except FileNotFoundError:
        print("File not found.")