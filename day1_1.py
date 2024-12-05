with open("inputs/day1/input.txt") as f:
    data = f.read().splitlines()

left = []
right = []
for pair in data:
    l, r = pair.split("   ")
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

diff = 0
for i in range(len(left)):
    diff += abs(left[i] - right[i])

print(diff)