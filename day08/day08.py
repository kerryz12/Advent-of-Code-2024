f = open("day07/day07.txt", "r")

input = f.read().splitlines()

rows = len(input)
cols = len(input[0])

antennas = {}

for y in range(rows):
    for x in range(cols):
        curr = input[y][x]
        
        if curr not in antennas:
            antennas[curr] = []
            
        antennas[curr].append((x, y))

def part1():
    ans = 0
    
    return ans
    
def part2():
    ans = 0
    
    return ans

print(part1())
print(part2())