f = open("day07/day07.txt", "r")

input = f.read().splitlines()

answers = []
values = []

for line in input:
    temp = line.split()
    
    answers.append(temp[0][:-1])
    values.append([int(t) for t in temp[1:]])

def backtrack(values, curr, index, answer):
    if index == len(values):
        return curr == answer
    
    if index == 0:
        return backtrack(values, values[0], 1, answer)
    
    if backtrack(values, curr + values[index], index + 1, answer):
        return True
        
    if backtrack(values, curr * values[index], index + 1, answer):
        return True
        
    return False

def backtrack2(values, curr, index, answer):
    if index == len(values):
        return curr == answer
    
    if index == 0:
        return backtrack2(values, values[0], 1, answer)
    
    if backtrack2(values, curr + values[index], index + 1, answer):
        return True
        
    if backtrack2(values, curr * values[index], index + 1, answer):
        return True

    concat = int(str(curr) + str(values[index]))
    if backtrack2(values, concat, index + 1, answer):
        return True
        
    return False

def part1():
    ans = 0

    for i in range(len(values)):
        if backtrack(values[i], 0, 0, int(answers[i])):
            ans += int(answers[i])
    
    return ans
    
def part2():
    ans = 0

    for i in range(len(values)):
        if backtrack2(values[i], 0, 0, int(answers[i])):
            ans += int(answers[i])
    
    return ans

print(part1())
print(part2())