f = open("day03/day03.txt", "r")

input = f.read().splitlines()

def part1():
    ans = 0

    for i in input:
        c = 0
        while c < len(i) - 2:
            if i[c:c+3] == "mul" and i[c+3] == '(':
                offset = c + 4
                while offset < len(i) and i[offset] != ')':
                    offset += 1
                
                if offset < len(i) and i[offset] == ')':
                    temp = i[c + 4:offset].split(',')
                    
                    if temp[0].isdigit() and temp[1].isdigit() and len(temp) == 2:
                        ans += int(temp[0]) * int(temp[1])
            
            c += 1

    return ans

def part2():
    ans = 0
    enable = 1

    for i in input:
        c = 0
        while c < len(i) - 2:
            if i[c:c+4] == "do()":
                enable = 1
            elif i[c:c+7] == "don't()":
                enable = 0
            
            if not enable:
                c += 1
                continue
            
            if i[c:c+3] == "mul" and i[c+3] == '(':
                offset = c + 4
                while offset < len(i) and i[offset] != ')':
                    offset += 1
                
                if offset < len(i) and i[offset] == ')':
                    temp = i[c + 4:offset].split(',')
                    
                    if temp[0].isdigit() and temp[1].isdigit() and len(temp) == 2:
                        ans += int(temp[0]) * int(temp[1])
            
            c += 1

    return ans    
                    
print(part1())
print(part2())                