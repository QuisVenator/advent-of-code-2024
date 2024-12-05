with open("inputs/day5/input.txt") as f:
    data = f.read().splitlines()

input_split = data.index("")
rules = [x.split("|") for x in data[:input_split]]
lists = [x.split(",") for x in data[input_split+1:]]

dag = {}
for i in range(len(rules)):
    if rules[i][0] not in dag:
        dag[rules[i][0]] = [rules[i][1]]
    else:
        if rules[i][1] not in dag[rules[i][0]]:
            dag[rules[i][0]].append(rules[i][1])

def check_valid(l, dag):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[j] in dag:
                if l[i] in dag[l[j]]:
                    return False
    return True

def fix_ordering(l, dag):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[j] in dag:
                if l[i] in dag[l[j]]:
                    l[i], l[j] = l[j], l[i]

result1 = 0
result2 = 0
for l in lists:
    if check_valid(l, dag):
        middlepage = l[len(l)//2]
        result1 += int(middlepage)
    else:
        fix_ordering(l, dag)
        middlepage = l[len(l)//2]
        result2 += int(middlepage)

print(f"Part 1: {result1}")
print(f"Part 2: {result2}")
        