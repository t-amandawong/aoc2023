
with open('input.txt', 'r') as file:
    steps = file.readline().strip().split(",")

hashes = []
for step in steps:
    current_value = 0
    for char in step:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    hashes.append(current_value)

print(hashes)
print(sum(hashes))

#part 2
boxes = {new_dict: {} for new_dict in range(256)}
for step in steps:
    current_value = 0
    current_string = ''
    for char in step:
        if char.isalpha():
            current_string += char
            current_value += ord(char)
            current_value *= 17
            current_value %= 256
        else:
            if char == '-':
                if current_string in boxes[current_value]:
                    del boxes[current_value][current_string]
            elif char == "=":
                continue
            else:
                boxes[current_value][current_string] = char
    # print(boxes)

focals = []
for box in boxes:
    box_num = box + 1
    for i, lens in enumerate(boxes[box]):
        slot_num = i + 1
        focal_length = int(boxes[box][lens])
        focusing_power = box_num * slot_num * focal_length
        # print(box_num, slot_num, focal_length)
        # print(focusing_power)
        focals.append(focusing_power)

print(focals)
print(sum(focals))