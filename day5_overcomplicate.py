with open("inputs/day5/input.txt") as f:
    data = f.read().splitlines()

input_split = data.index("")
rules = [x.split("|") for x in data[:input_split]]
lists = [x.split(",") for x in data[input_split+1:]]

dag = {}
result = 0
for i in range(len(rules)):
    if rules[i][0] not in dag:
        dag[rules[i][0]] = [rules[i][1]]
    else:
        if rules[i][1] not in dag[rules[i][0]]:
            dag[rules[i][0]].append(rules[i][1])

def bfs(dag, start, visited, sub_visited):
    if start in visited:
        return False
    if start not in dag:
        return True
    
    for x in dag[start]:
        if x not in sub_visited:
            sub_visited.add(x)
            if not bfs(dag, x, visited, sub_visited):
                print(f"Rules state {start} must be visited before {x} (visited: {visited})")
                return False
    return True

for i, l in enumerate(lists):
    visited = set()

    valid = True
    for x in l:
        print(f"Checking {x}")
        sub_visited = set() 
        valid = bfs(dag, x, visited, sub_visited)
        if not valid:
            exit()
            break
        visited.add(x)
    
    if valid:
        middlepage = l[len(l)//2]
        result += int(middlepage)

print(result)
    
        

