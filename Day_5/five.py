def part1():
    protocols = {}

    protocols_input = open("protocols.txt", "r")

    # populate dictionaru with protocols
    for line in protocols_input:
        vals = line.split("|")
        if vals[0] not in protocols:
            protocols[vals[0]] = [vals[1][:2]]
        else:
            protocols[vals[0]].append(vals[1][:2])

    # validate updates
    updates_input = open("updates.txt", "r")
    total = 0

    for line in updates_input:
        line = line.split(",")
        if len(line[-1]) > 2:
            line[-1] = line[-1][:2]

        valid = True

        for num in range(len(line)):
            for i in range(num):
                if line[num] in protocols:
                    if line[i] in protocols[line[num]]:
                        valid = False
                        break
            if not valid:
                break
        
        if valid:
            total += int(line[len(line) // 2])

    return total

def part2():
    protocols = {}

    protocols_input = open("protocols.txt", "r")

    # populate dictionary with protocols
    for line in protocols_input:
        vals = line.split("|")
        if vals[0] not in protocols:
            protocols[vals[0]] = [vals[1][:2]]
        else:
            protocols[vals[0]].append(vals[1][:2])

    # validate updates

    # def checkValid(index, arr):
    #     for i in range(index):
            
    updates_input = open("updates.txt", "r")
    total = 0

    for line in updates_input:
        line = line.split(",")
        if len(line[-1]) > 2:
            line[-1] = line[-1][:2]

        valid = True

        for num in range(len(line)):
            for i in range(num):
                if line[num] in protocols:
                    if line[i] in protocols[line[num]]:
                        temp = line[i]
                        line[i] = line[num]
                        line[num] = temp
                        valid = False
        
        if not valid:
            total += int(line[len(line) // 2])
        

    return total

print("Part 1: ", part1())
print("Part 2: ", part2())