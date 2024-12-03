# Pair up the smallest number in the left list with the smallest number in the right list, 
# then the second-smallest left number with the second-smallest right number, and so on.
# Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances

def part1():
    f = open("input.txt", "r")

    first, second = [], []

    for line in f:
        x = line.split("   ")
        first.append(int(x[0]))
        second.append(int(x[1]))

    first.sort()
    second.sort()

    distance = 0

    for i in range(len(first)):
        distance += abs(first[i] - second[i])

    return distance


def part2():
    similarity = 0

    f = open("input.txt", "r")

    first, second = [], {}

    for line in f:
        x = line.split("   ")
        first.append(int(x[0]))
        key = int(x[1])

        if key not in second:
            second[key] = 1
        else:
            second[key] += 1

    for i in first:
        if i in second:
            similarity += second[i] * i
            
    return similarity

print("Part 1: ", part1())
print("Part2: ", part2())
