
def part1():
    def checkSpot(row, col, crossword):
        # needs to check all eight directions
        total = 0
        word = ['X', 'M', 'A', 'S']

        #if row > 2:           
        valid = True    # Check up
        for i in range(4):  
            if not (0 <= row - i < len(crossword) and 0 <= col < len(crossword[0])): 
                valid = False
            if word[i] != crossword[row - i][col]:
                valid = False
        if valid:
            total += 1
        
        if row < len(crossword) - 3:           # Check down
            valid = True
            for i in range(4): 
                if not (0 <= row + i < len(crossword) and 0 <= col < len(crossword[0])): 
                    valid = False
                elif word[i] != crossword[row + i][col]:
                    valid = False
            if valid:
                total += 1

        if col > 2:           # Check left
            valid = True
            for i in range(4):  
                if not (0 <= row < len(crossword) and 0 <= col - i < len(crossword[0])): 
                    valid = False
                elif word[i] != crossword[row][col  - i]:
                    valid = False
            if valid:
                total += 1

        if col < len(crossword[row]) - 3:           # Check right
            valid = True
            for i in range(4): 
                if not (0 <= row < len(crossword) and 0 <= col + i < len(crossword[0])): 
                    valid = False 
                elif word[i] != crossword[row][col + i]:
                    valid = False
            if valid:
                total += 1
        
        if row < len(crossword) - 3 and col < len(crossword[row]) - 3:      # check down right
            valid = True
            for i in range(4): 
                if not (0 <= row + i < len(crossword) and 0 <= col + i < len(crossword[0])): 
                    valid = False  
                elif word[i] != crossword[row + i][col + i]:
                    valid = False
            if valid:
                total += 1
        
        if row < len(crossword) - 3 and col > 2:                # check down left
            valid = True
            for i in range(4):  
                if not (0 <= row + i < len(crossword) and 0 <= col - i < len(crossword[0])): 
                    valid = False 
                elif word[i] != crossword[row + i][col - i]:
                    valid = False
            if valid:
                total += 1

        if row > 2 and col < len(crossword[row]) - 3:       # check up right
            valid = True
            for i in range(4):  
                if not (0 <= row - i < len(crossword) and 0 <= col + i < len(crossword[0])): 
                    valid = False 
                elif word[i] != crossword[row - i][col + i]:
                    valid = False
            if valid:
                total += 1

        if row > 2 and col > 2:                     # check up left
            valid = True
            for i in range(4): 
                if not (0 <= row - i < len(crossword) and 0 <= col - i < len(crossword[0])): 
                    valid = False  
                elif word[i] != crossword[row - i][col - i]:
                    valid = False
            if valid:
                total += 1
        return total

    input = open("input.txt", "r")

    crossword = []

    for line in input:
        crossword.append(line[:-1])
        #print(len(line[:-1]))
    crossword[-1] += 'S'

    total = 0
    for row in range(len(crossword)):
        for col in range(len(crossword[row])):
            if crossword[row][col] == 'X':
                total += checkSpot(row, col, crossword)

    return total

def part2():
    input = open("input.txt", "r")

    crossword = []

    for line in input:
        crossword.append(line[:-1])
    crossword[-1] += 'S'

    def checkSpot(row, col, arr):
        if (((arr[row - 1][col - 1] == 'S' and arr[row + 1][col + 1] == 'M') or (arr[row - 1][col - 1] == 'M' and arr[row + 1][col + 1] == 'S')) and ((arr[row -1][col + 1] == 'S' and arr[row + 1][col - 1] == 'M') or  (arr[row -1][col + 1] == 'M' and arr[row + 1][col - 1] == 'S'))):
            return 1
        return 0
    
    total = 0

    for row in range(1, len(crossword) - 1):
        for col in range(1, len(crossword[row]) - 1):
            if crossword[row][col] == 'A':
                total += checkSpot(row, col, crossword)

    return total

print("Part 1: ", part1())
print("Part 2: ", part2())