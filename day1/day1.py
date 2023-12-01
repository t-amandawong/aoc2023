# aoc day 1 2023!!!

calibration_sum = 0
with open('puzzle_input.txt', 'r') as in_file:
    for line in in_file:
        if line.strip():
            calib = [i for i in line.strip() if i.isdigit()]
            full_num = int(calib[0] + calib[-1])
            # print(full_num)
            calibration_sum += full_num

print(calibration_sum)

# part 2
nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

nums_dict = {}
for i in range(len(nums)):
    nums_dict[nums[i]] = str(i + 1)

#print(nums_dict)

all_calibs = 0
with open('puzzle_input.txt', 'r') as in_file:
    for line in in_file:
        #print(line.strip() + ":", end=' ')
        valid_calibs = {}
        if line.strip():
            for num in nums:
                if line.find(num) != -1:
                    all_matches = [i for i in range(len(line.strip())) if line.strip().startswith(num, i)]
                    for index in all_matches:
                        valid_calibs[index] = nums_dict.get(num)
            for i in range(len(line)):
                if line[i].isdigit():
                    valid_calibs[i] = line[i]
            sorted_calibs = dict(sorted(valid_calibs.items()))
            #print(sorted_calibs)

            first_index = list(sorted_calibs.keys())[0]
            last_index = list(sorted_calibs.keys())[-1]

            full_calib = sorted_calibs[first_index] + sorted_calibs[last_index]
            #print(int(full_calib))
            all_calibs += int(full_calib)

print(all_calibs)