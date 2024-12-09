def part1():
    input_file = open("input.txt", "r")

    disk_map = ""

    for line in input_file:
        disk_map = line

    isFile = True
    ID = 0
    blocks = []

    for num in disk_map:
        if isFile:
            for i in range(int(num)):
                blocks.append(ID)
            ID += 1
        else:
            for i in range(int(num)):
                blocks.append('.')
        isFile = not isFile

    left, right = 0, len(blocks) - 1

    while (left < right):
        while (left < right and blocks[left] != '.'):
            left += 1
        while (right > left and blocks[right] == '.'):
            right -= 1
        
        if (left < right):
            temp = blocks[left]
            blocks[left] = blocks[right]
            blocks[right] = temp
        
        left += 1
        right -= 1


    position = 0
    total = 0

    while blocks[position] != '.':
        total += position * blocks[position]
        position += 1

    return total

def part2():
    input_file = open("input.txt", "r")

    disk_map = ""

    for line in input_file:
        disk_map = line

    isFile = True
    ID = 0
    blocks = []

    for num in disk_map:
        if isFile:
            for i in range(int(num)):
                blocks.append(ID)
            ID += 1
        else:
            for i in range(int(num)):
                blocks.append('.')
        isFile = not isFile

    left, right = 0, len(blocks) - 1

    while (left < right):
        print(left, right)
        while (left < right and blocks[left] != '.'):
            left += 1
        while (right > left and blocks[right] == '.'):
            right -= 1
        
        val_size = 1
        val = blocks[right]

        while right - val_size > left and blocks[right - val_size] == val:
            val_size += 1 

        shifted = False
        temp_left = left
        while not shifted and temp_left < right:
            while temp_left < right and blocks[temp_left] != '.':
                temp_left += 1

            slot_size = 1

            while temp_left + slot_size < right and blocks[temp_left + slot_size] == '.':
                slot_size += 1
            
            if val_size <= slot_size:
                for i in range(val_size):
                    blocks[temp_left + i] = val
                    blocks[right - i] = '.'
                shifted = True
                right -= val_size
               # print(left)
            else:
                temp_left += slot_size
        
        if shifted == False:
            right -= val_size


    position = 0
    total = 0

    while position < len(blocks):
        if blocks[position] != '.':
            total += position * blocks[position]
        position += 1

    with open("output.txt", "w") as f:
        print(blocks, file=f)
    return total


print("Part 1: ", part1())
print("Part2: ", part2())