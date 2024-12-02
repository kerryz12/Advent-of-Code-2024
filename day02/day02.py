f = open("day02/day02.txt", "r")

input = f.read().splitlines()

def safe(row):
    increasing = 1
    decreasing = 1
    
    for i in range(len(row) - 1):
        if 0 < row[i+1] - row[i] <= 3:
            continue
        
        increasing = 0
        break
    
    for i in range(len(row) - 1):
        if 0 < row[i] - row[i+1] <= 3:
            continue
        
        decreasing = 0
        break
    
    return increasing or decreasing


def part1():
    ans = 0
    
    for i in input:
        curr = list(map(int, i.split()))
        
        if safe(curr):
            ans += 1
            
    return ans

def part2():
    ans = 0
    
    for i in input:
        curr = list(map(int, i.split()))
        
        if safe(curr):
            ans += 1
        else:
            for i in range(len(curr)):
                if safe(curr[:i] + curr[i + 1:]):
                    ans += 1
                    break
                
    return ans

print(part1())
print(part2())