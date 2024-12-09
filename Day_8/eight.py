def part1():   
    input_file = open("input.txt", "r")

    installation = []
    for line in input_file:
        if line[-1] == "\n":
            line = line[:-1]
        line = list(line)
        installation.append(line)

    def checkForAntinodes(row, col, installation):
        start_row, start_col = row // 2, col // 2
        end_row, end_col = row + ((len(installation) - row) // 2) - 1, col + ((len(installation[0]) - col) // 2) - 1
        antinodes = 0

        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                if not (i == row and j == col) and installation[i][j][0] == installation[row][col][0]: # checks if spot is same antenna type
                    temp_row, temp_col = row + 2 *(i - row), col + 2 * (j - col)

                    if len(installation[temp_row][temp_col]) == 1:
                        antinodes += 1
                        installation[temp_row][temp_col] += '#'
        
        return antinodes

    total_antinodes = 0

    for row in range(len(installation)):
        for col in range(len(installation[0])):
            if installation[row][col][0] != '.':
                total_antinodes += checkForAntinodes(row, col, installation)

    # prints final installation with antinodes labeled

    # for line in installation:
    #     for i in line:
    #         if len(i) == 1:
    #             print(i, end="  ")
    #         else:
    #             print(i, end=" ")
    #     print()

    return total_antinodes


def part2():  
    input_file = open("input.txt", "r")

    installation = []
    for line in input_file:
        if line[-1] == "\n":
            line = line[:-1]
        line = list(line)
        installation.append(line)

    def checkForAntinodes(row, col, installation):
        start_row, start_col = 0, 0
        end_row, end_col = len(installation) - 1, len(installation[0]) - 1
        antinodes = 0

        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                if not (i == row and j == col) and installation[i][j][0] == installation[row][col][0]: # checks if spot is same antenna type
                    diff_row, diff_col = i - row, j - col

                    temp_row, temp_col = row + diff_row, col + diff_col

                    while (temp_row >= start_row and temp_row <= end_row) and (temp_col >= start_col and temp_col <= end_col):
                        if len(installation[temp_row][temp_col]) == 1:
                            antinodes += 1
                            installation[temp_row][temp_col] += '#'
                        
                        temp_row += diff_row
                        temp_col += diff_col
                    
                    temp_row = row - diff_row
                    temp_col = col - diff_col

                    while (temp_row >= start_row and temp_row <= end_row) and (temp_col >= start_col and temp_col <= end_col):
                        if len(installation[temp_row][temp_col]) == 1:
                            antinodes += 1
                            installation[temp_row][temp_col] += '#'
                        
                        temp_row -=  diff_row
                        temp_col -= diff_col
                    
        
        return antinodes

    total_antinodes = 0

    for row in range(len(installation)):
        for col in range(len(installation[0])):
            if installation[row][col][0] != '.':
                total_antinodes += checkForAntinodes(row, col, installation)

    #prints final installation with antinodes labeled

    # for line in installation:
    #     for i in line:
    #         if len(i) == 1:
    #             print(i, end="  ")
    #         else:
    #             print(i, end=" ")
    #     print()

    return total_antinodes

print("Part 1: ", part1())
print("Part 2: ", part2())