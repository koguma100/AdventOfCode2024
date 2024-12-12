def part1():
    input_file = open("input.txt", "r")

    top_map = []

    for line in input_file:

        if line[-1] == "\n":
            line = line[:-1]
        line = list(line)
        for i in range(len(line)):
            line[i] = int(line[i])
        top_map.append(line)

    def dfs(row, col, ends):
        if top_map[row][col] == 9 and [row, col] not in ends:
            ends.append([row,col])
            return

        if row - 1 >= 0 and top_map[row - 1][col] == top_map[row][col] + 1:
            dfs(row - 1, col, ends)
        
        if col - 1 >= 0 and top_map[row][col - 1] == top_map[row][col] + 1:
            dfs(row, col - 1, ends)
        
        if row + 1 < len(top_map) and top_map[row + 1][col] == top_map[row][col] + 1:
            dfs(row + 1, col, ends)
        
        if col + 1 < len(top_map[row]) and top_map[row][col + 1] == top_map[row][col] + 1:
            dfs(row, col + 1, ends)


    total = 0

    for row in range(len(top_map)):
        for col in range(len(top_map[row])):
            if top_map[row][col] == 0:
                ends = []
                dfs(row, col, ends)
                total += len(ends)

    return total

def part2():
    input_file = open("input.txt", "r")

    top_map = []

    for line in input_file:

        if line[-1] == "\n":
            line = line[:-1]
        line = list(line)
        for i in range(len(line)):
            line[i] = int(line[i])
        top_map.append(line)

    def dfs(row, col):
        total = 0

        if top_map[row][col] == 9:
            return 1

        if row - 1 >= 0 and top_map[row - 1][col] == top_map[row][col] + 1:
            total += dfs(row - 1, col)
        
        if col - 1 >= 0 and top_map[row][col - 1] == top_map[row][col] + 1:
            total += dfs(row, col - 1)
        
        if row + 1 < len(top_map) and top_map[row + 1][col] == top_map[row][col] + 1:
            total += dfs(row + 1, col)
        
        if col + 1 < len(top_map[row]) and top_map[row][col + 1] == top_map[row][col] + 1:
            total += dfs(row, col + 1)
        
        return total


    total = 0

    for row in range(len(top_map)):
        for col in range(len(top_map[row])):
            if top_map[row][col] == 0:
                total += dfs(row, col)

    return total

print("Part 1: ", part1())
print("Part 2: ", part2())