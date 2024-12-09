with open("inputs/day6/input.txt") as f:
    data = f.read().splitlines()

data = [list(x) for x in data]
directions = [[-1,0],[0,1],[1,0],[0,-1]]
obstacle_positions = set()
current_pos = [0,0]
direction = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] in ["^", ">", "v", "<"]:
            current_pos = [i,j]
            
            direction = ["^", ">", "v", "<"].index(data[i][j])
            data[i][j] = "X"
start = current_pos
start_direction = direction

def has_loop(d, start_pos):
    collisions = set()
    pos = [start_pos[0], start_pos[1]]
    looped = False
    while True:
        next_pos = [pos[0] + directions[d][0], pos[1] + directions[d][1]]
        if next_pos[0] < 0 or next_pos[0] >= len(data) or next_pos[1] < 0 or next_pos[1] >= len(data[0]):
            break
        if data[next_pos[0]][next_pos[1]] == "#":
            if (next_pos[0], next_pos[1], d) in collisions:
                looped = True
                break
            else:
                collisions.add((next_pos[0], next_pos[1], d))
                d = (d + 1) % 4
        else:
            pos = [next_pos[0], next_pos[1]]
    return looped
    

result1 = 1
steps = 0
while True:
    steps += 1
    next_pos = [current_pos[0] + directions[direction][0], current_pos[1] + directions[direction][1]]
    if next_pos[0] < 0 or next_pos[0] >= len(data) or next_pos[1] < 0 or next_pos[1] >= len(data[0]):
        break
    
    if data[next_pos[0]][next_pos[1]] == "#":
        direction = (direction + 1) % 4
    else:
        current_pos = [next_pos[0], next_pos[1]]
        if data[current_pos[0]][current_pos[1]] == ".":
            result1 += 1
            data[current_pos[0]][current_pos[1]] = "X"

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "X":
            data[i][j] = "#"
            if has_loop(start_direction, start):
                obstacle_positions.add((i,j))
                data[i][j] = "O"
            else:
                data[i][j] = "X"

if (start[0], start[1]) in obstacle_positions:
    obstacle_positions.remove((start[0], start[1]))

for i in range(len(data)):
    print("".join(data[i]))

print(f"Part 1: {result1}")
print(f"Part 2: {len(obstacle_positions)}")