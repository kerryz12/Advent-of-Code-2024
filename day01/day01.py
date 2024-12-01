f = open("day01/day01.txt", "r")

input = f.read().splitlines()
num1 = []
num2 = []

for i in input:
    temp = i.split()
    num1.append(int(temp[0]))
    num2.append(int(temp[1]))
    
num1.sort()
num2.sort()

ans = 0

for i in range(len(num1)):
    ans += abs(num1[i] - num2[i])
    
print(ans)

hm = {}

for n in num2:
    if n not in hm:
        hm[n] = 1
    else:
        hm[n] += 1
    
ans = 0    
    
for n in num1:
    if n in hm:
        ans += n * hm[n]
    
print(ans)