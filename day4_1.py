data = []
with open("inputs/day4/input.txt") as f:
    data = f.read().splitlines()

# Indexes:
# 0: Horizontal normal
# 1: Horizontal reverse
# 2: Vertical normal
# 3: Vertical reverse
# 4: Diagonal LR normal
# 5: Diagonal LR reverse
# 6: Diagonal RL normal
# 7: Diagonal RL reverse
valid = []
for line in data:
    valid.append([])
    for c in line:
        valid[-1].append([
            c == "X",
            c == "S",
            c == "X",
            c == "S",
            c == "X",
            c == "S",
            c == "X",
            c == "S",
        ])

# Add a blank row and column to the top and left and right
for i in range(len(valid)):
    valid[i].insert(0, [False] * 8)
    valid[i].append([False] * 8)
valid.insert(0, [[False] * 8 for _ in range(len(valid[0]))])

# Also add blank lines to data
data.insert(0, "")
for i in range(len(data)):
    data[i] = " " + data[i] + " "

# XMAS
prev = {
    "M": "X",
    "A": "M",
    "S": "A"
}
prev_reverse = {
    "X": "M",
    "M": "A",
    "A": "S"
}

count = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        c = data[i][j]
        if c in prev:
            # horizontal normal
            if valid[i][j-1][0] and data[i][j-1] == prev[c]:
                valid[i][j][0] = True
                if c == "S":
                    count += 1
            
            # vertical normal
            if valid[i-1][j][2] and data[i-1][j] == prev[c]:
                valid[i][j][2] = True
                if c == "S":
                    count += 1
            
            # diagonal LR normal
            if valid[i-1][j-1][4] and data[i-1][j-1] == prev[c]:
                valid[i][j][4] = True
                if c == "S":
                    count += 1
            
            # diagonal RL normal
            if valid[i-1][j+1][6] and data[i-1][j+1] == prev[c]:
                valid[i][j][6] = True
                if c == "S":
                    count += 1
        if c in prev_reverse:
            # horizontal reverse
            if valid[i][j-1][1] and data[i][j-1] == prev_reverse[c]:
                valid[i][j][1] = True
                if c == "X":
                    count += 1
            
            # vertical reverse
            if valid[i-1][j][3] and data[i-1][j] == prev_reverse[c]:
                valid[i][j][3] = True
                if c == "X":
                    count += 1
            
            # diagonal LR reverse
            if valid[i-1][j-1][5] and data[i-1][j-1] == prev_reverse[c]:
                valid[i][j][5] = True
                if c == "X":
                    count += 1

            # diagonal RL reverse
            if valid[i-1][j+1][7] and data[i-1][j+1] == prev_reverse[c]:
                valid[i][j][7] = True
                if c == "X":
                    count += 1

print(count)