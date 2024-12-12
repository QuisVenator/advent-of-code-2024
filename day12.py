with open("inputs/day12/input.txt") as f:
    lines = f.read().splitlines()

lines = [line for line in lines if line]

# Split into characters and add a 0 at start and end
lines = [['0'] + list(line) + ['0'] for line in lines]

# Add a row of 0s at start and end
lines = [['0'] * len(lines[0])] + lines + [['0'] * len(lines[0])]

# Create a copy of the lines with boolean values
used = [[c == '0' for c in line] for line in lines]

def calc_cost(lines, used, y, x, c) -> tuple[int, int]:
    if used[y][x]:
        return 0, 0

    if lines[y][x] != c:
        return 0, 0
    
    used[y][x] = True
    area = 1
    perimeter = 0

    if lines[y][x+1] == c:
        a, p = calc_cost(lines, used, y, x+1, c)
        area += a
        perimeter += p
    else:
        perimeter += 1
    
    if lines[y][x-1] == c:
        a, p = calc_cost(lines, used, y, x-1, c)
        area += a
        perimeter += p
    else:
        perimeter += 1

    if lines[y+1][x] == c:
        a, p = calc_cost(lines, used, y+1, x, c)
        area += a
        perimeter += p
    else:
        perimeter += 1

    if lines[y-1][x] == c:
        a, p = calc_cost(lines, used, y-1, x, c)
        area += a
        perimeter += p
    else:
        perimeter += 1
    
    return area, perimeter

cost = 0
for y in range(1, len(lines) - 1):
    for x in range(1, len(lines[0]) - 1):
        if not used[y][x]:
            area, perimeter = calc_cost(lines, used, y, x, lines[y][x])
            cost += area * perimeter

print(f"Part 1: {cost}")
    