f = open("day08/day08.txt", "r")

input = f.read().splitlines()

rows = len(input)
cols = len(input[0])

antennas = {}

for y in range(rows):
    for x in range(cols):
        curr = input[y][x]
        
        if curr == '.':
            continue
        
        if curr not in antennas:
            antennas[curr] = []
            
        antennas[curr].append((x, y))

def part1():
    ans = 0
    antinodes = set()
    
    for key, val in antennas.items():
        if len(val) <= 1:
            continue
                
        for i in range(len(val)):
            for j in range(i + 1, len(val)):
                dx = val[j][0] - val[i][0]
                dy = val[j][1] - val[i][1]
                
                antinode1 = (val[i][0] - dx, val[i][1] - dy)
                if 0 <= antinode1[0] < cols and 0 <= antinode1[1] < rows:
                    if antinode1 not in antinodes:
                        antinodes.add(antinode1)
                        ans += 1
                    
                antinode2 = (val[j][0] + dx, val[j][1] + dy)
                if 0 <= antinode2[0] < cols and 0 <= antinode2[1] < rows:
                    if antinode2 not in antinodes:
                        antinodes.add(antinode2)
                        ans += 1
    
    return ans
    
def part2():
    ans = 0
    antinodes = set()
    
    for key, val in antennas.items():
        if len(val) <= 1:
            continue
                
        for i in range(len(val)):
            for j in range(i + 1, len(val)):
                dx = val[j][0] - val[i][0]
                dy = val[j][1] - val[i][1]
                
                antinode1 = (val[i][0], val[i][1])
                while True:
                    if 0 <= antinode1[0] < cols and 0 <= antinode1[1] < rows:
                        if antinode1 not in antinodes:
                            antinodes.add(antinode1)
                            ans += 1
                            
                        antinode1 = (antinode1[0] - dx, antinode1[1] - dy)
                    else:
                        break

                antinode2 = (val[j][0], val[j][1])
                while True:
                    if 0 <= antinode2[0] < cols and 0 <= antinode2[1] < rows:
                        if antinode2 not in antinodes:
                            antinodes.add(antinode2)
                            ans += 1
                            
                        antinode2 = (antinode2[0] + dx, antinode2[1] + dy)
                    else:
                        break
    
    return ans

print(part1())
print(part2())