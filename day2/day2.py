max_red = 12
max_green = 13
max_blue = 14

games = list()
with open('input.txt') as in_file:
    for line in in_file:
        if line.strip:
            stripped_line = line.strip()
            game = stripped_line.split(": ")[1].split("; ")
            games.append(game)

valid_games = list()
min_powers = list()
for i in range(len(games)):
    curr_red = 0
    curr_blue = 0
    curr_green = 0
    for subgame in games[i]:
        colors = subgame.split(", ")
        for color in colors:
            num_color = color.split()
            num = int(num_color[0])
            if num_color[1] == 'red':
                if num > curr_red:
                    curr_red = num
            if num_color[1] == 'blue':
                if num > curr_blue:
                    curr_blue = num
            if num_color[1] == 'green':
                if num > curr_green:
                    curr_green = num
    # for part 1
    if curr_red <= max_red and curr_blue <= max_blue and curr_green <= max_green:
        valid_games.append(i+1)
    # for part 2
    min_powers.append(curr_red * curr_blue * curr_green)


print(sum(valid_games))
print(sum(min_powers))