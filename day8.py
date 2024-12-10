import math

with open("inputs/day8/input.txt") as f:
    lines = f.read().splitlines()

lines = [line for line in lines if line]
# print(lines)

frequencies = {}
antinodes = set()
resonant_antinodes = set()

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == ".":
            continue
        if c not in frequencies:
            frequencies[c] = []
        frequencies[c].append((i, j))


def simplify_fraction(n1, n2):
    div = math.gcd(n1, n2)
    return n1 // div, n2 // div

for k, v in frequencies.items():
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            smaller_x = min(v[i][0], v[j][0])
            bigger_x = max(v[i][0], v[j][0])
            smaller_y = min(v[i][1], v[j][1])
            bigger_y = max(v[i][1], v[j][1])

            diff_x = bigger_x - smaller_x
            diff_y = bigger_y - smaller_y
            diff_x_simplified, diff_y_simplified = simplify_fraction(diff_x, diff_y)
            antinode1 = ()
            antinode2 = ()

            dir_lr = "down"
            if smaller_x == v[i][0]:
                if smaller_y == v[i][1]:
                    antinode1 = (smaller_x - diff_x, smaller_y - diff_y)
                    antinode2 = (bigger_x + diff_x, bigger_y + diff_y)
                else:
                    antinode1 = (smaller_x - diff_x, bigger_y + diff_y)
                    antinode2 = (bigger_x + diff_x, smaller_y - diff_y)
                    dir_lr = "up"
            else:
                if smaller_y == v[j][1]:
                    antinode1 = (smaller_x - diff_x, smaller_y - diff_y)
                    antinode2 = (bigger_x + diff_x, bigger_y + diff_y)
                else:
                    antinode1 = (smaller_x - diff_x, bigger_y + diff_y)
                    antinode2 = (bigger_x + diff_x, smaller_y - diff_y)
                    dir_lr = "up"
            
            node = (v[i][0], v[i][1])
            resonant_antinodes.add(node)
            while node[0] >= 0 and node[0] < len(lines) and node[1] >= 0 and node[1] < len(lines[0]):
                resonant_antinodes.add(node)
                if dir_lr == "down":
                    node = (node[0] - diff_x_simplified, node[1] - diff_y_simplified)
                else:
                    node = (node[0] - diff_x_simplified, node[1] + diff_y_simplified)
            node = (v[j][0], v[j][1])
            while node[0] >= 0 and node[0] < len(lines) and node[1] >= 0 and node[1] < len(lines[0]):
                resonant_antinodes.add(node)
                if dir_lr == "down":
                    node = (node[0] + diff_x_simplified, node[1] + diff_y_simplified)
                else:
                    node = (node[0] + diff_x_simplified, node[1] - diff_y_simplified)
            
            antinodes.add(antinode1)
            antinodes.add(antinode2)

out_of_bounds = set()
for node in antinodes:
    if node[0] < 0 or node[0] >= len(lines) or node[1] < 0 or node[1] >= len(lines[0]):
        out_of_bounds.add(node)
    else:
        lines[node[0]] = lines[node[0]][:node[1]] + "#" + lines[node[0]][node[1]+1:]

for line in lines:
    print(line)

for line in lines:
    line = line.replace("#", ".")

for node in resonant_antinodes:
    lines[node[0]] = lines[node[0]][:node[1]] + "#" + lines[node[0]][node[1]+1:]

print()
for line in lines:
    print(line)

print(f"Part 1: {len(antinodes) - len(out_of_bounds)}")
print(f"Part 2: {len(resonant_antinodes)}")