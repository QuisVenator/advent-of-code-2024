with open("inputs/day1/input.txt") as f:
# with open("inputs/day1/testinput.txt") as f:
    data = f.read().splitlines()

left = []
right = []
for pair in data:
    l, r = pair.split("   ")
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

# Hack for the last element
right.append(float("inf"))

i = 0
j = 0
last_add = 0
last_id = 0
similarity = 0
while i < len(left):
    if left[i] == last_id:
        similarity += last_add
        i += 1
    elif left[i] < right[j]:
        last_id = left[i]
        last_add = 0
        i += 1
    elif left[i] > right[j]:
        last_add = 0
        j += 1
    else:
        last_id = left[i]
        last_add = 0
        while left[i] == right[j]:
            last_add += left[i]
            j += 1

print(similarity)