

with open('input.txt', 'r') as file:
    cards = [line.strip().split(':')[1] for line in file]

total_points = 0
wins = []
for card in cards:
    first, second = card.split('|')
    my_nums = first.split()
    winning_nums = second.split()
    num_wins = 0
    # print(my_nums, winning_nums)
    for num in my_nums:
        if num in winning_nums:
            # print(num)
            num_wins += 1
    if num_wins > 0:
        total_points += pow(2, num_wins - 1)
    wins.append(num_wins)

print(total_points)

copies = [1] * len(wins)
for i in range(len(wins)):
    if wins[i] > 0:
        for it in range(1, wins[i] + 1):
            copies[i + it] += copies[i]

# print(wins)
# print(copies)
print(sum(copies))