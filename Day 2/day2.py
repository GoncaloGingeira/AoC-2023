def get_valid_games(max_red, max_green, max_blue, games_info):
    
    game_list = []
    for line in games_info:
        meta = {"gameID": int(line.split(": ")[0].split(" ")[1]), "info": get_game_info(line)}
        game_list.append(meta)
    valid_games = []
    for game in game_list:
        if game["info"]["red"] <= max_red and game["info"]["green"] <= max_green and game["info"]["blue"] <= max_blue:
            valid_games.append(game["gameID"])
            
    return valid_games

def get_game_info(line):

    line = line.split(": ")[1]

    rounds = line.split("; ")

    info = {
        "blue": 0,
        "red": 0,
        "green": 0
    }

    for round in rounds:
        colors = round.split(", ")

        for color in colors:
            number, color = color.split(" ")
            info[color] = max(info[color], int(number))

    return info

def get_game_powers(input_lines):
    sum_of_powers = 0
    for input_str in input_lines:
        game_info = get_game_info(input_str)
        sum_of_powers += game_info["red"] * game_info["green"] * game_info["blue"]
    return sum_of_powers
    
if __name__ == "__main__":
    file_name = input("Enter the name of the text file: ")
    try:
        with open(file_name, 'r') as file:
            input_lines = file.readlines()
        input_lines = [x.strip() for x in input_lines]
        
        max_red = 12
        max_green = 13
        max_blue = 14

        result = get_valid_games(max_red, max_green, max_blue, input_lines)
        print("Valid games IDs:", result)
        print("Sum of IDs:", sum(result))
        sum_of_powers = get_game_powers(input_lines)
        print("Sum of Powers:", sum_of_powers)
    except FileNotFoundError:
        print("File not found.")