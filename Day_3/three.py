def part1():
    def validateSubstring(substring):
        num1, num2 = 0, 0
        i = 0
        if not len(substring) < 3:
            while i < len(substring) and substring[i] != ',':
                i += 1
            if (i > 0 and i < 4) and ''.join(substring[:i]).isdigit(): 
                num1 = int(''.join(substring[:i]))
            else:
                return [0, 0]
            i += 1
            if (len(substring) - i > 0 and len(substring) - i < 4) and ''.join(substring[i:]).isdigit():
                num2 = int(''.join(substring[i:]))
            else:
                return [0, 0]


        return [num1, num2]

    total = 0
    input = open("input.txt", "r")

    for line in input:
        valid = ['m', 'u', 'l', '(']
        curr = 0

        for c in range(len(line)):
            if line[c] == valid[curr]:
                curr += 1
                if curr == 4:
                    substring = []
                    tempIndex = c + 1
                    while tempIndex < len(line) and line[tempIndex] != ')':
                        substring.append(line[tempIndex])
                        tempIndex += 1
                    if tempIndex != len(line):
                        result = validateSubstring(substring)
                        total += result[0] * result[1]
                    curr = 0
            else:
                curr = 0
    return total

def part2():
    def validateSubstring(substring):
        num1, num2 = 0, 0
        i = 0
        if not len(substring) < 3:
            while i < len(substring) and substring[i] != ',':
                i += 1
            if (i > 0 and i < 4) and ''.join(substring[:i]).isdigit(): 
                num1 = int(''.join(substring[:i]))
            else:
                return [0, 0]
            i += 1
            if (len(substring) - i > 0 and len(substring) - i < 4) and ''.join(substring[i:]).isdigit():
                num2 = int(''.join(substring[i:]))
            else:
                return [0, 0]


        return [num1, num2]

    total = 0
    enabled = True
    input = open("input.txt", "r")

    for line in input:
        valid = ['m', 'u', 'l', '(']
        do = "do()"
        dont = "don't()"
        curr = 0

        for c in range(len(line)):
            if enabled and line[c] == valid[curr]:
                curr += 1
                if curr == 4:
                    substring = []
                    tempIndex = c + 1
                    while tempIndex < len(line) and line[tempIndex] != ')':
                        substring.append(line[tempIndex])
                        tempIndex += 1
                    if tempIndex != len(line):
                        result = validateSubstring(substring)
                        total += result[0] * result[1]
                    curr = 0
            else:
                if c < len(line) - 7 and line[c:c+7] == dont:
                    enabled = False
                elif c < len(line) - 4 and line[c:c+4] == do:
                    enabled = True
                curr = 0
    return total

print("Part 1: ", part1())
print("Part 2: ", part2())
