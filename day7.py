with open("inputs/day7/input.txt") as f:
    lines = f.read().replace(":", "").splitlines()

data = []
for line in lines:
    line = line.split(" ")
    data.append([int(x) for x in line])

# print(data)

def calc(nums, i, res):
    if i == len(nums):
        return res == nums[0]
    if i > len(nums):
        # Shoudn't happen
        return False
    if res > nums[0]:
        return False
    
    if calc(nums, i+1, res+nums[i]):
        return True
    return calc(nums, i+1, res*nums[i])

def calc_or_concat(nums, i, res):
    if i == len(nums):
        return res == nums[0]
    if i > len(nums):
        # Shoudn't happen
        return False
    if res > nums[0]:
        return False
    
    if calc_or_concat(nums, i+1, res+nums[i]):
        return True
    if calc_or_concat(nums, i+1, res*nums[i]):
        return True
    return calc_or_concat(nums, i+1, int(str(res) + str(nums[i])))

possible = []
possible_with_concat = []
calibration_result = 0
calibration_result_with_concat = 0
for eq in data:
    if calc(eq, 2, eq[1]):
        possible.append(eq)
        calibration_result += eq[0]
    elif calc_or_concat(eq, 2, eq[1]):
        possible_with_concat.append(eq)
        calibration_result_with_concat += eq[0]

print(f"Part 1: {calibration_result}")
print(f"Part 2: {calibration_result_with_concat + calibration_result}")