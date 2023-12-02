# aoc day 1 2023!!!

with open('puzzle_input.txt', 'r') as in_file:
    lines = [line.strip() for line in in_file]

# part 1: each line contains a specific calibration value that is found by combining the first and last digit.
# find each line's calibration value and submit the sum of all the calibration values
calibration_sum = 0
for line in lines:
    digit = [i for i in line if i.isdigit()]
    calib = int(digit[0] + digit[-1])
    calibration_sum += calib

print("Part 1:", calibration_sum)

# part 2: digits written out as "one", "two", "three", and so on, also count as digits
# find each line's new calibration value (still first and last, but now including string words)
# submit the sum of all the calibration values
nums_dict = {'one': '1',
             'two': '2',
             'three': '3',
             'four': '4',
             'five': '5',
             'six': '6',
             'seven': '7',
             'eight': '8',
             'nine': '9'}

true_sum = 0
for line in lines:
    # valid_digits stores the index where each valid digit is along with the digit itself in 'index: digit' pair
    valid_digits = {}
    # check for string nums and add its index and digit version into valid_digits dictionary
    for num in nums_dict.keys():
        if line.find(num) != -1:
            all_matches = [i for i in range(len(line)) if line.startswith(num, i)]
            for index in all_matches:
                valid_digits[index] = nums_dict.get(num)
    # check for digit nums and its index and digit itself into valid_digits dictionary
    for i in range(len(line)):
        if line[i].isdigit():
            valid_digits[i] = line[i]

    # sort valid_digits by index & find first and last
    sorted_digits = dict(sorted(valid_digits.items()))
    first_index = list(sorted_digits.keys())[0]
    last_index = list(sorted_digits.keys())[-1]

    # find full_calib by concatenating first and last digits
    full_calib = sorted_digits[first_index] + sorted_digits[last_index]
    true_sum += int(full_calib)

print("Part 2:", true_sum)