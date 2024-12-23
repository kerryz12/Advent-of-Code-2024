f = open("day04/day04.txt", "r")

input = f.read().splitlines()

directions = [
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
]

def part1():
    ans = 0
        
    def check(x, y, dx, dy):
        if not (0 <= x + 3 * dx < len(input[0]) and 0 <= y + 3 * dy < len(input)):
            return False
        
        target = "XMAS"
        for i in range(4):
            nx, ny = x + i * dx, y + i * dy
            if input[ny][nx] != target[i]:
                return False
            
        return True
    
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == 'X':
                for dx, dy in directions:
                    if check(x, y, dx, dy):
                        ans += 1
            
    return ans

def part2():
    ans = 0
    
    def check(x, y):
        if x < 1 or y < 1 or x > len(input[0]) - 2 or y > len(input) - 2:
            return False
    
        word1 = input[y - 1][x - 1] + input[y][x] + input[y + 1][x + 1]
        word2 = input[y - 1][x + 1] + input[y][x] + input[y + 1][x - 1]
        
        patterns = {"MAS", "SAM"}
        return (word1 in patterns and word2 in patterns)
        
    for y in range(len(input)):
        for x in range(len(input[0])):
            if check(x, y):
                ans += 1
    
    return ans

print(part1())
print(part2())