
def part1():    
    input_file = open("input.txt", "r")
    total = 0

    for line in input_file:
        line = line.split(":")
        test_value = int(line[0])

        if line[1][-1] == "\n":
            line[1] = line[1][:-1]
        nums = line[1].split(" ")[1:]

        for i in range(len(nums)):
            nums[i] = int(nums[i])

        possible_vals = [[nums[0]]]

        for i in range(1, len(nums)):
            newVals = []
            for num in possible_vals[i - 1]:
                if num * nums[i] <= test_value:
                    newVals.append(num * nums[i])
                if num + nums[i] <= test_value:
                    newVals.append(num + nums[i])
            possible_vals.append(newVals)
        
        if test_value in possible_vals[-1]:
            total += test_value

    return total

def part2():
    input_file = open("input.txt", "r")
    total = 0

    for line in input_file:
        line = line.split(":")
        test_value = int(line[0])

        if line[1][-1] == "\n":
            line[1] = line[1][:-1]
        nums = line[1].split(" ")[1:]

        for i in range(len(nums)):
            nums[i] = int(nums[i])

        possible_vals = [[nums[0]]]

        for i in range(1, len(nums)):
            newVals = []
            for num in possible_vals[i - 1]:
                if num * nums[i] <= test_value:
                    newVals.append(num * nums[i])
                if num + nums[i] <= test_value:
                    newVals.append(num + nums[i])
                concatenated = int(str(num) + str(nums[i]))
                if concatenated <= test_value:
                    newVals.append(concatenated)
            possible_vals.append(newVals)
        
        if test_value in possible_vals[-1]:
            total += test_value

    return total

print("Part1: ", part1())
print("Part2: ", part2())