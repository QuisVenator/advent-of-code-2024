with open("inputs/day12/exampleinput.txt") as f:
    lines = f.read().splitlines()

lines = [line for line in lines if line]

# Split into characters and add a 0 at start and end
lines = [['0'] + list(line) + ['0'] for line in lines]

# Add a row of 0s at start and end
lines = [['0'] * len(lines[0])] + lines + [['0'] * len(lines[0])]

# Create a copy of the lines with boolean values
used = [[c == '0' for c in line] for line in lines]

def calc_cost(lines, used, y, x, c):
    if used[y][x]:
        return 0, 0, 0

    if lines[y][x] != c:
        return 0, 0, 0
    
    used[y][x] = True
    area = 1
    perimeter = 0
    corners = 0

    # Perimeter and area calculation
    if lines[y][x+1] == c:
        a, p, corn = calc_cost(lines, used, y, x+1, c)
        area += a
        perimeter += p
        corners += corn
    else:
        perimeter += 1
    
    if lines[y][x-1] == c:
        a, p, corn = calc_cost(lines, used, y, x-1, c)
        area += a
        perimeter += p
        corners += corn
    else:
        perimeter += 1

    if lines[y+1][x] == c:
        a, p, corn = calc_cost(lines, used, y+1, x, c)
        area += a
        perimeter += p
        corners += corn
    else:
        perimeter += 1

    if lines[y-1][x] == c:
        a, p, corn = calc_cost(lines, used, y-1, x, c)
        area += a
        perimeter += p
        corners += corn
    else:
        perimeter += 1

    # Corner calculation
    # There are 8 possible corners
    # 4 convex and 4 concave
    # Convex examples:
    #    0000
    #    0110
    #    0110
    #    0000
    # Concave examples:
    #    0000000
    #    0001000
    #    0011100
    #    0001000
    #    0000000

    # Convex, top left
    if lines[y-1][x] != c and lines[y][x-1] != c:
        corners += 1
    # Convex, top right
    if lines[y-1][x] != c and lines[y][x+1] != c:
        corners += 1
    # Convex, bottom left
    if lines[y+1][x] != c and lines[y][x-1] != c:
        corners += 1
    # Convex, bottom right
    if lines[y+1][x] != c and lines[y][x+1] != c:
        corners += 1
    # Concave, top left
    if lines[y-1][x] == c and lines[y][x-1] == c and lines[y-1][x-1] != c:
        corners += 1
    # Concave, top right
    if lines[y-1][x] == c and lines[y][x+1] == c and lines[y-1][x+1] != c:
        corners += 1
    # Concave, bottom left
    if lines[y+1][x] == c and lines[y][x-1] == c and lines[y+1][x-1] != c:
        corners += 1
    # Concave, bottom right
    if lines[y+1][x] == c and lines[y][x+1] == c and lines[y+1][x+1] != c:
        corners += 1

    return area, perimeter, corners

cost1 = 0
cost2 = 0
for y in range(1, len(lines) - 1):
    for x in range(1, len(lines[0]) - 1):
        if not used[y][x]:
            area, perimeter, corners = calc_cost(lines, used, y, x, lines[y][x])
            cost1 += area * perimeter
            cost2 += area * corners

print(f"Part 1: {cost1}")
print(f"Part 2: {cost2}")
    