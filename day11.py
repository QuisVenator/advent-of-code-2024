import dataclasses

@dataclasses.dataclass
class Stone:
    val: int
    next: object

    def update(self):
        if self.val == 0:
            self.val = 1
        elif len(str(self.val)) % 2 == 0:
            n = self.next
            s = str(self.val)
            self.val = int(s[:len(s)//2])
            self.next = Stone(int(s[len(s)//2:]), n)
        else:
            self.val *= 2024

with open("inputs/day11/exampleinput.txt") as f:
    lines = f.read().splitlines()

stones = lines[0].split(" ")

head = Stone(int(stones[0]), None)
current = head
for stone in stones[1:]:
    current.next = Stone(int(stone), None)
    current = current.next

blinks = 6
for i in range(blinks):
    current = head
    while current:
        next = current.next
        current.update()
        current = next
    
    # current = head
    # print(current.val, end=" ")
    # while current.next:
    #     current = current.next
    #     print(current.val, end=" ")
    # print()
    print(f"blinked {i+1} times")

current = head
stone_count = 1
while current.next:
    stone_count += 1
    current = current.next

print(f"Part 1: {stone_count}")
