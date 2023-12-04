import os

max_red = 12
max_green = 13
max_blue = 14


file = open(os.path.dirname(__file__) + '/input.txt', 'r')
games = file.read().split('\n')
possible_games_ids = []
powers_of_min_games = []
for game in games:
    rounds = game.split(';')
    index = 5
    first_round = rounds[0]
    id = ''
    while first_round[index].isnumeric():
        id += first_round[index]
        index += 1

    possible_games_ids.append(int(id))
    first_round = first_round[index + 2:]

    min_red = 0
    min_green = 0
    min_blue = 0
    for round in rounds:
        blue_num = 0
        red_num = 0
        green_num = 0
        num = 0
        i = 0
        while i < len(round):
            c = round[i]
            if c.isnumeric():
                num = c
                if round[i+1].isnumeric():
                    num += round[i+1]
                    i += 1
                i += 1
                num = int(num)
            elif c == 'b':
                blue_num += num
                num = 0
                i += 4
            elif c == 'r':
                red_num += num
                num = 0
                i += 3
            elif c == 'g':
                green_num += num
                num = 0
                i += 5
            else:
                i += 1
        if blue_num > min_blue:
            min_blue = blue_num
        if green_num > min_green:
            min_green = green_num
        if red_num > min_red:
            min_red = red_num
        
        
        if blue_num > max_blue or red_num > max_red or green_num > max_green:
            if int(id) in possible_games_ids:
                possible_games_ids.remove(int(id))
    powers_of_min_games.append(min_blue * min_red * min_green)
print(f"Sum of possible games ids => {sum(possible_games_ids)}")
print(f"Sum of power of min possible cubes => {sum(powers_of_min_games)}")