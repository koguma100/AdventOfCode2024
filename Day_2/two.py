# The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only 
# tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.


def part1():
    input = open("input.txt", "r")
    total_safe_reports = 0

    for line in input:
        increasing = True
        is_safe = True
        x = line.split(" ")
        for i in range(len(x)):
            x[i] = int(x[i])

        if x[0] - x[1] > 0:
            increasing = False

        for i in range(len(x) - 1):
            if increasing and (x[i] - x[i + 1] > -1 or x[i] - x[i + 1] < -3):
                is_safe = False
                break
            elif not increasing and (x[i] - x[i + 1] < 1 or x[i] - x[i + 1] > 3):
                is_safe = False
                break

        if is_safe:
            total_safe_reports += 1

    return total_safe_reports

def part2():
    input = open("input.txt", "r")
    total_safe_reports = 0

    def is_safe(report):
        increasing = True
        safe = True

        for i in range(len(report)):
            report[i] = int(report[i])

        if report[0] - report[1] > 0:
            increasing = False

        for i in range(len(report) - 1):
            if increasing and (report[i] - report[i + 1] > -1 or report[i] - report[i + 1] < -3):
                safe = False
                break
            elif not increasing and (report[i] - report[i + 1] < 1 or report[i] - report[i + 1] > 3):
                safe = False
                break

        return safe
    
    for line in input:
        safe_report = False
        x = line.split(" ")
        for i in range(len(x)):
            x[i] = int(x[i])

        for i in range(len(x)):
            temp = x[i]
            x.pop(i)
            print(x)
            if is_safe(x):
                safe_report = True
            x.insert(i, temp)
        
        if safe_report:
            total_safe_reports += 1
        
    return total_safe_reports

print("Part 1: ", part1())
print("Part2: ", part2())