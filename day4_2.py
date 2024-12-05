data = []
with open("inputs/day4/input.txt") as f:
    data = f.read().splitlines()

count = 0
for i in range(1, len(data) - 1):
    for j in range(1, len(data[i]) - 1):
        if data[i][j] == "A":
            if ((data[i-1][j-1] == "M" and data[i+1][j+1] == "S" or
                 data[i-1][j-1] == "S" and data[i+1][j+1] == "M") and
                (data[i+1][j-1] == "M" and data[i-1][j+1] == "S" or
                 data[i+1][j-1] == "S" and data[i-1][j+1] == "M")):
                count += 1

print(count)
