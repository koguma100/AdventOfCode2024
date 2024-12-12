def part1():
    input_file = open("input.txt", "r")

    stones = []
    for line in input_file:
        stones = line

    stones = stones.split(" ")

    for blink in range(25):
        newStones = []
        for i in range(len(stones)):
            if stones[i] == '0':
                newStones.append('1')
            elif len(stones[i]) % 2 == 0:
                # if str(stones[i][len(stones[i]) // 2:]) == '0':
                #     print(str(int(stones[i][:len(stones[i]) // 2])), str(int(stones[i][len(stones[i]) // 2:])))
                newStones.append(str(int(stones[i][:len(stones[i]) // 2])))
                newStones.append(str(int(stones[i][len(stones[i]) // 2:])))
            else:
                newStones.append(str(int(stones[i]) * 2024))
        stones = newStones

    #print(stones)
    return len(stones)

# part1 solution too slow, must use DP memoization approach
def part2():
    input_file = open("input.txt", "r")

    stones = []
    for line in input_file:
        stones = line

    stones = stones.split(" ")
    total = 0
    for i in range(len(stones)):
        stones[i] = int(stones[i])
    cache = {}

    def dp(num, t):
        res = 0
        if (num, t) in cache:
            return cache[(num, t)]
        if t == 0:
            res = 1
        elif num == 0:
            res = dp(1, t - 1)
        elif len(str(num)) % 2 == 0:
            left = int(str(num)[:len(str(num)) // 2])
            right = int(str(num)[len(str(num)) // 2:])
            res = dp(left, t - 1) + dp(right, t - 1)
        else:
            res = dp(num * 2024, t - 1)
        cache[(num, t)] = res
        return res
    
    total = 0
    for stone in stones:
        total += dp(stone, 75)
    return total

print("Part 1: ", part1())
print("Part 2: ", part2())