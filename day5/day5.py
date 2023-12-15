
with open('test.txt', 'r') as file:
    lines = [line.strip() for line in file]

seeds = [int(seed) for seed in lines[0].split(':')[1].split()]

seeds_changes = [False] * len(seeds)
for line in lines:
    if line == '':
        seeds_changes = [False for _ in seeds_changes]
        continue
    if line[0].isdigit():
        destination, source, rang = [int(num) for num in line.split()]
        for i in range(len(seeds)):
            if seeds[i] in range(source, source + rang) and seeds_changes[i] is False:
                offset = seeds[i] - source
                seeds[i] = destination + offset
                seeds_changes[i] = True
    # else:
    #     print(line.split('-')[0])
    #     print(seeds)
print(seeds)
print(min(seeds))

# part 2
seeds = [int(seed) for seed in lines[0].split(':')[1].split()]
seeds_ranges = []
first = 0
for i in range(len(seeds)):
    if i % 2 == 0:
        first = seeds[i]
    else:
        seeds_ranges.append((first, first + seeds[i]))

ranges_changes = [False] * len(seeds_ranges)
intersections = []
print(seeds_ranges)
for line in lines:
    if line == '':
        ranges_changes = [False] * len(seeds_ranges)
        continue
    if line[0].isdigit():
        destination, source, rang = [int(num) for num in line.split()]
        print(source, source + rang)
        for i in range(len(seeds_ranges)):
            seed = seeds_ranges[i]
            low = max(seed[0], source)
            high = min(seed[1], source + rang)
            if low < high:
                offset_low = low - source
                offset_high = high - source
                new_range = (destination + offset_low, destination + offset_high)
                if source <= low and source + rang >= high:
                    seeds_ranges[i] = new_range