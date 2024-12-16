with open("inputs/day13/input.txt") as f:
    lines = f.read().splitlines()

lines = [line.replace(",", "").replace("X+", "").replace("Y+", "").replace("X=", "").replace("Y=", "") for line in lines if line]
lines = [line.split(":")[1] for line in lines]
lines = [line.split(" ")[1:] for line in lines]
lines = [[int(x) for x in line] for line in lines]

print(len(lines))


def solve(A, B, P):
    min_cost = 10000
    i = 0
    while i * A[0] <= P[0] and i * A[1] <= P[1]:
        remainder_x = P[0] - i * A[0]
        remainder_y = P[1] - i * A[1]
        if remainder_x % B[0] == 0 and remainder_y % B[1] == 0 and remainder_x // B[0] == remainder_y // B[1]:
            min_cost = min(min_cost, i*3 + remainder_x//B[0])
    
    return min_cost if min_cost != 10000 else 0

total_cost = 0
for i in range(0, len(lines), 3):
    res = solve(lines[i], lines[i+1], [lines[i+2][0] + 10000000000000, lines[i+2][1]+10000000000000])
    # print(res)
    total_cost += res
    print(i)

print(total_cost)