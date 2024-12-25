f = open("day06/day06.txt", "r")

input = f.read().splitlines()

rows, cols = len(input), len(input[0])

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
seen = set()

for j in range(rows):
    for i in range(cols):
        if input[j][i] == '^':
            start_x, start_y = i, j
            break

def part1():
    ans = 0
    
    x, y = start_x, start_y
    direction = 0
                
    while 0 <= x < cols and 0 <= y < rows:
        if (x, y) not in seen:
            seen.add((x, y))
            ans += 1

        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy

        if 0 <= nx < cols and 0 <= ny < rows and input[ny][nx] != '#':
            x, y = nx, ny
            
        elif 0 <= nx < cols and 0 <= ny < rows:
            direction = (direction + 1) % 4
            
        else:
            break
                
    return ans
    
def detect_loop(grid):
    loop_seen = set()
    x, y = start_x, start_y
    direction = 0
        
    while True:
        state = (x, y, direction)
        
        if state in loop_seen:
            return True
            
        if not (0 <= x < cols and 0 <= y < rows):
            return False
            
        loop_seen.add(state)
        
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] != '#':
            x, y = nx, ny
            
        elif 0 <= nx < cols and 0 <= ny < rows:
            direction = (direction + 1) % 4
            
        else:
            return False

def part2():        
    ans = 0
    seen_list = list(seen)

    for coords in seen_list:
        x, y = coords
        
        if (x, y) == (start_x, start_y):
            continue
            
        grid = [list(row) for row in input]
        grid[y][x] = '#'
        
        if detect_loop(grid):
            ans += 1
                    
    return ans
    
print(part1())
print(part2())