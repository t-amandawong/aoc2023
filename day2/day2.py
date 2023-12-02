# aoc day 2 2023

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

# each line is a game in which colored cubes (red, green, or blue) are shown in multiple sets
# add a list of each game's sets to the larger games list
games = list()
with open('input.txt') as in_file:
    for line in in_file:
        if line.strip:
            game = line.strip().split(": ")[1].split("; ")
            games.append(game)

# in part 1, add up the IDs for each game that is possible if the bag only contains 12 red, 13 green, and 14 blue
# the IDs(each game's index in games list + 1) will be stored in valid_games list, and its sum will be submitted

# in part 2, for each game, find the minimum amount of cubes needed for each color to make the game possible
# the powers for each game(product of min red, min green, and min blue cubes) will be stored in powers list
# the sum of the powers list is submitted for part 2
valid_games = list()
powers = list()
for i in range(len(games)):
    # initialize the current max for each color to 0 for every game
    curr_red = 0
    curr_green = 0
    curr_blue = 0
    # for each set, split the string to just the number and color combinations
    for cube_sets in games[i]:
        num_colors = cube_sets.split(", ")
        for num_colors in num_colors:
            num, color = num_colors.split()
            num = int(num)
            # check which color the number corresponds to and update curr_color accordingly
            if color == 'red':
                curr_red = max(curr_red, num)
            if color == 'green':
                curr_green = max(curr_green, num)
            if color == 'blue':
                curr_blue = max(curr_blue, num)
    # (part 1) check that the current value for each color is less than its max, and add to valid_games if so
    if curr_red <= MAX_RED and curr_green <= MAX_GREEN and curr_blue <= MAX_BLUE:
        valid_games.append(i+1)
    # (part 2) the minimum amount needed to play each game is actually the max of each color, so
    # multiply each current_color together to obtain the power for this game
    powers.append(curr_red * curr_blue * curr_green)

print("Part 1:", sum(valid_games))
print("Part 2:", sum(powers))