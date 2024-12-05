with open("inputs/day2/input.txt") as f:
    data = f.read().splitlines()

data = [[int(y) for y in x.split(" ")] for x in data]

safe_count = 0
for report in data:
    if report[0] == report[1]:
        continue

    maxdiff = 3
    mindiff = 1
    if report[0] > report[1]:
        maxdiff = -1
        mindiff = -3
    
    valid = True
    for i in range(1, len(report)):
        if not mindiff <= report[i] - report[i-1] <= maxdiff:
            valid = False
            break
    if valid:
        safe_count += 1

print(safe_count)