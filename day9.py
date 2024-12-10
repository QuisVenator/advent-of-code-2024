with open("inputs/day9/exampleinput.txt") as f:
    lines = f.read().splitlines()

input = lines[0]

disk = []
for i in range(len(input)):
    if i % 2 == 0:
        disk.append((i//2, int(input[i])))
    else:
        disk.append((-1, int(input[i])))

ori_disk = disk.copy()

blockwise_compressed_disk = []
endp = len(disk) - 1
for i in range(len(disk)):
    if disk[i][0] != -1 and disk[i][1] != 0:
        blockwise_compressed_disk.append(disk[i])
    else:
        free_space = disk[i][1]
        while free_space > 0:
            if disk[endp][0] == -1:
                endp -= 1
            if endp <= i:
                break
            
            if disk[endp][1] <= free_space:
                blockwise_compressed_disk.append((disk[endp][0], disk[endp][1]))
                free_space -= disk[endp][1]
                disk[endp] = (disk[endp][0], 0)
                endp -= 1
            else:
                blockwise_compressed_disk.append((disk[endp][0], free_space))
                disk[endp] = (disk[endp][0], disk[endp][1] - free_space)
                free_space = 0

disk = ori_disk.copy()
filewise_compressed_disk = []
last_unassigned = len(disk) - 1
for i in range(len(disk)):
    if disk[i][0] != -1 and disk[i][1] != 0:
        filewise_compressed_disk.append(disk[i])
    else:
        free_space = disk[i][1]

        while disk[last_unassigned][0] == -1 or disk[last_unassigned][1] == 0:
            last_unassigned -= 1
        endp = last_unassigned
        while endp > i and free_space > 0:
            print(f"endp: {endp}, free_space: {free_space}")
            if disk[endp][0] != -1 and disk[endp][1] <= free_space and disk[endp][1] != 0:
                free_space -= disk[endp][1]
                filewise_compressed_disk.append((disk[endp][0], disk[endp][1]))
                
                disk[endp] = (-1, disk[endp][1])

                to_assign = endp-1
                while to_assign > 0 and disk[to_assign][0] == -1:
                    to_assign -= 1
                to_assign += 1

                next_free_space = endp
                while next_free_space < len(disk) and disk[next_free_space][0] == -1:
                    disk[to_assign] = (-1, disk[to_assign][1] + disk[next_free_space][1])
                    disk[next_free_space] = (-1, 0)
                    next_free_space += 1
            endp -= 1
        if free_space > 0:
            filewise_compressed_disk.append((-1, free_space))
                

blockwise_checksum = 0
real_i = 0
for i in range(len(blockwise_compressed_disk)):
    for j in range(blockwise_compressed_disk[i][1]):
        blockwise_checksum += real_i * blockwise_compressed_disk[i][0]
        real_i += 1

filewise_checksum = 0
real_i = 0
for i in range(len(filewise_compressed_disk)):
    for j in range(filewise_compressed_disk[i][1]):
        filewise_checksum += real_i * filewise_compressed_disk[i][0]
        real_i += 1

print(blockwise_compressed_disk)
print(filewise_compressed_disk)
print(f"Part 1: {blockwise_checksum}")
print(f"Part 2: {filewise_checksum}")
