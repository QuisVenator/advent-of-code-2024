with open("inputs/day2/input.txt") as f:
    data = f.read().splitlines()

data = [[int(y) for y in x.split(" ")] for x in data]

def is_safe(report, reverse):
    maxdiff = 3
    mindiff = 1
    if reverse:
        maxdiff = -1
        mindiff = -3
    
    dampener_used = False
    i = 0
    while i < len(report) - 1:
        if not mindiff <= report[i+1] - report[i] <= maxdiff:
            if dampener_used:
                return False
            dampener_used = True

            # check if we skip i or i+1
            if i+2 == len(report):
                # We are at last element, just drop it
                i += 1
            # When we can continue without i+1 do it
            elif mindiff <= report[i+2] - report[i] <= maxdiff:
                i += 2
            # When we can continue without i do it
            elif i == 0 or mindiff <= report[i+1] - report[i-1] <= maxdiff:
                i += 1
        else:
            i += 1
        
    return True

safe_count = 0
for report in data:
    if is_safe(report, False) or is_safe(report, True):
        safe_count += 1

print(safe_count)

