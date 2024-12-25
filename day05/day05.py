f = open("day05/day05.txt", "r")

input = f.read().splitlines()

separator = input.index('')

rules = {}
for line in input[:separator]:
    before, after = line.split('|')
    
    if before not in rules:
        rules[before] = set()
        
    rules[before].add(after)

updates = []

for line in input[separator+1:]:
    updates.append(line.split(','))

def is_valid(pages, rules):
    for i, before in enumerate(pages):
        for after in pages[i+1:]:
            if before in rules and after in rules[before]:
                return False
            
    return True

def part1():
    ans = 0
        
    for update in updates:
        flag = True
        
        for i in range(len(update)):
            before = update[i]
            
            if before in rules:                
                for j in range(i + 1, len(update)):
                    after = update[j]
                    
                    if after in rules and before in rules[after]:
                        flag = False
                        break
            
            if not flag:
                break
                
        if flag:
            ans += int(update[len(update) // 2])
    
    return ans

def part2():
    ans = 0
        
    for update in updates:
        flag = True
        
        for i in range(len(update)):
            before = update[i]
            
            if before in rules:                
                for j in range(i + 1, len(update)):
                    after = update[j]
                    
                    if after in rules and before in rules[after]:
                        flag = False
                        break
            
            if not flag:
                break
               
        if not flag:
            sorted_update = update.copy()
            
            while True:
                swapped = False
                for i in range(len(sorted_update) - 1):
                    for j in range(i + 1, len(sorted_update)):
                        if (sorted_update[i] in rules and sorted_update[j] in rules[sorted_update[i]]):
                            sorted_update[i], sorted_update[j] = sorted_update[j], sorted_update[i]
                            swapped = True
                
                if not swapped:
                    break
            
            ans += int(sorted_update[len(sorted_update) // 2])
    
    return ans

print(part1())
print(part2())
