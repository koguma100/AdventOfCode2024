
def part1():
    input_file = open("input.txt", "r")

    maze = []

    for line in input_file:
        if line[-1] == "\n":
            line = line[:-1]
        maze.append(list(line))

    NUM_ROWS, NUM_COLS = len(maze), len(maze[0])

    def move(x, y):
        maze[x][y] = 'X'
        directions = [( -1, 0 ), ( 0, 1 ), ( 1, 0 ), ( 0, -1 )]   
        current_direction = 0
        distinct_positions = 1

        while (x + directions[current_direction][0] > -1 and x + directions[current_direction][0] < NUM_COLS) and (y + directions[current_direction][1]> -1 and y + directions[current_direction][1]< NUM_ROWS):
            if (maze[x + directions[current_direction][0]][y + directions[current_direction][1]] == '#'):
                current_direction = (current_direction + 1) % 4
            else:
                if maze[x + directions[current_direction][0]][y + directions[current_direction][1]] == '.':
                    distinct_positions += 1
                    maze[x + directions[current_direction][0]][y + directions[current_direction][1]] = 'X'
                x += directions[current_direction][0]
                y += directions[current_direction][1]
        return distinct_positions

    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            if maze[row][col] != '#' and maze[row][col] != '.':
                print(row, col)
                return move(row, col)
            

def part2():
    input_file = open("input.txt", "r")
    maze = []

    for line in input_file:
        if line[-1] == "\n":
            line = line[:-1]
        maze.append(list(line))

    NUM_ROWS, NUM_COLS = len(maze), len(maze[0])

    def checkForLoop():
        x, y = 52, 80       # hard coded start :p
        directions = [( -1, 0 ), ( 0, 1 ), ( 1, 0 ), ( 0, -1 )]   
        current_direction = 0
        visited = {(52, 80, 0)} # positions notated (row, col, direction)

        while (x + directions[current_direction][0] > -1 and x + directions[current_direction][0] < NUM_COLS) and (y + directions[current_direction][1]> -1 and y + directions[current_direction][1]< NUM_ROWS):
            if (maze[x + directions[current_direction][0]][y + directions[current_direction][1]] == '#'):
                current_direction = (current_direction + 1) % 4
            else:
                x += directions[current_direction][0]
                y += directions[current_direction][1]
                curr = (x, y, current_direction)
                if curr in visited:
                    return False
                visited.add(curr)

        return True
    
    total = 0

    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            if maze[row][col] != '#':
                maze[row][col] = '#'
                print(row, col)
                if not checkForLoop():
                    total += 1
                maze[row][col] = '.'

    return total

print("Part 1: ", part1())
print("Part 2: ", part2())  # Takes a while but gets there 
                