# aoc day 3 2023

symbols = dict()
numbers = dict()
gears = list()
lines = []

with open('input.txt') as in_file:
    for line in in_file:
        lines.append(line)

for i in range(len(lines)):
    if lines[i].strip():
        line = lines[i].strip()
        current_num = ""
        for j in range(len(line)):
            if line[j].isdigit():
                current_num += line[j]
                if j == len(line) - 1:
                    numbers[(i, j)] = current_num
            else:
                if current_num != "":
                    numbers[(i, j - 1)] = current_num
                    current_num = ""
                if line[j] != '.':
                    symbols[(i, j)] = line[j]
                    # part 2 :
                    if line[j] == '*':
                        gears.append((i, j))

# print(symbols)
# print(numbers)
# print(gears)

# part 1
valid_nums = []
for i, j in numbers.keys():
    j_start = j - len(numbers[(i, j)]) + 1
    # print("i: " + str(i) + ", j end: " + str(j) + ", j start: " + str(j_start))
    for si, sj in symbols.keys():
        if abs(si - i) <= 1 and sj in range(j_start - 1, j + 2):
            valid_nums.append(int(numbers[(i, j)]))
            #print(int(numbers[(i, j)]))

print(sum(valid_nums))

# part 2
gear_ratios = []
for i, j in gears:
    part_nums = []
    for ni, nj in numbers.keys():
        nj_start = nj - len(numbers[ni, nj]) + 1
        if abs(i - ni) <= 1 and j in range(nj_start - 1, nj + 2):
            part_nums.append(int(numbers[(ni, nj)]))
            # print(numbers[(ni, nj)])
    if len(part_nums) == 2:
        gear_ratios.append(part_nums[0] * part_nums[1])

print(sum(gear_ratios))