with open("inputs/day13/input.txt") as f:
    lines = f.read().splitlines()

lines = [line.replace(",", "").replace("X+", "").replace("Y+", "").replace("X=", "").replace("Y=", "") for line in lines if line]
lines = [line.split(":")[1] for line in lines]
lines = [line.split(" ")[1:] for line in lines]
lines = [[int(x) for x in line] for line in lines]

print(len(lines))

def solve_multi_possible(A, B, P):
    # We have two basic cases with three subcases each:
    # 1. The A button moves us so much, that using it is cheaper than using the B button (meaning A > 3*B)
    #   1.1 We can reach the price without ever using the B button
    #   1.2 We need to use the B button at least once
    #   1.3 We can´t reach the price
    # 2. The B button moves us so much, that using it is cheaper than or the same as using the A button (meaning A <= 3*B)
    #   2.1 We can reach the price without ever using the A button
    #   2.2 We need to use the A button at least once
    #   2.3 We can´t reach the price

    # Case 1
    if A[0] > 3 * B[0]:
        print("Case 1")
        # Case 1.1
        if P[0] % A[0] == 0 and P[1] % A[1] == 0:
            if P[0] // A[0] == P[1] // A[1]:
                return P[0] // A[0] * 3
            # We can´t reach the price
            else:
                return 0
        # Case 1.2
        else:
            if P[0] % A[0] == B[0] and P[1] % A[1] == B[1]:
                return P[0] // A[0] * 3 + 1
            else:
                return 0
    # Case 2
    else:
        # Case 2.1
        if P[0] % B[0] == 0 and P[1] % B[1] == 0:
            if P[0] // B[0] == P[1] // B[1]:
                return P[0] // B[0]
            else:
                return 0
        # Case 2.2
        else:
            if P[0] % B[0] == A[0] and P[1] % B[1] == A[1]:
                return P[0] // B[0] + 3
            else:
                return 0

def solve_efficient(A, B, P):
    nominator = A[0] * P[1] - P[0] * A[1]
    denominator = A[0] * B[1] - B[0] * A[1]

    if denominator == 0:
        return solve_multi_possible(A, B, P)

    if nominator % denominator != 0:
        return 0
    else:
        n = nominator // denominator
        if (P[0] - n * B[0]) % A[0] != 0:
            return 0
        m = (P[0] - n * B[0]) // A[0]
        return 3 * m + n

total_cost_p1 = 0
total_cost_p2 = 0
for i in range(0, len(lines), 3):
    res = solve_efficient(lines[i], lines[i+1], [lines[i+2][0], lines[i+2][1]])
    total_cost_p1 += res

    conversion_error = 10000000000000
    res = solve_efficient(lines[i], lines[i+1], [lines[i+2][0] + conversion_error, lines[i+2][1] + conversion_error])
    total_cost_p2 += res

print(f"Part 1: {total_cost_p1}")
print(f"Part 2: {total_cost_p2}")