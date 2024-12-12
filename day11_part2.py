dp = {}

def blink_stone(val, iterations):
    if iterations == 0:
        return 1
    if (val, iterations) in dp:
        return dp[(val, iterations)]

    orig_val = val
    val2 = 0
    split = False
    if val == 0:
        val = 1
    elif len(str(val)) % 2 == 0:
        s = str(val)
        val = int(s[:len(s)//2])
        val2 = int(s[len(s)//2:])
        split = True
    else:
        val *= 2024
    
    count = blink_stone(val, iterations - 1)
    # print(f"val: {val}, val2: {val2}, count: {count}")
    if split:
        count += blink_stone(val2, iterations - 1)
    
    dp[(orig_val, iterations)] = count
    return count


with open("inputs/day11/input.txt") as f:
    lines = f.read().splitlines()

stones = lines[0].split(" ")
stones = [int(stone) for stone in stones]

blinks = 75

result = 0
for stone in stones:
    result += blink_stone(stone, blinks)

print(f"Part 1: {result}")
