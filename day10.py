with open("inputs/day10/input.txt") as f:
    lines = f.read().splitlines()

map = [line for line in lines if line]
map = [[int(c) for c in line] for line in map]
breadcumbs = [[0 for _ in range(len(map[0]))] for _ in range(len(map))]

def hike(map, x, y, breadcumbs, bread_index):
    if breadcumbs[x][y] == bread_index:
        return 0
    breadcumbs[x][y] = bread_index
    if map[x][y] == 9:
        return 1
    
    score = 0
    if x > 0 and map[x-1][y] == map[x][y] + 1:
        score += hike(map, x-1, y, breadcumbs, bread_index)
    if x < len(map) - 1 and map[x+1][y] == map[x][y] + 1:
        score += hike(map, x+1, y, breadcumbs, bread_index)
    if y > 0 and map[x][y-1] == map[x][y] + 1:
        score += hike(map, x, y-1, breadcumbs, bread_index)
    if y < len(map[0]) - 1 and map[x][y+1] == map[x][y] + 1:
        score += hike(map, x, y+1, breadcumbs, bread_index)
    
    return score

def rate(map, x, y):
    if map[x][y] == 9:
        return 1
    
    score = 0
    if x > 0 and map[x-1][y] == map[x][y] + 1:
        score += rate(map, x-1, y)
    if x < len(map) - 1 and map[x+1][y] == map[x][y] + 1:
        score += rate(map, x+1, y)
    if y > 0 and map[x][y-1] == map[x][y] + 1:
        score += rate(map, x, y-1)
    if y < len(map[0]) - 1 and map[x][y+1] == map[x][y] + 1:
        score += rate(map, x, y+1)
    
    return score

result1 = 0
result2 = 0
counter = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        counter += 1
        if map[i][j] == 0:
            score = hike(map, i, j, breadcumbs, counter)
            rating = rate(map, i, j)
            print(f"Start at {i}, {j}, score: {score}, rating: {rating}")
            result1 += score
            result2 += rating

print(f"Part 1: {result1}")
print(f"Part 2: {result2}")