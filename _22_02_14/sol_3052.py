
temp = 0
tempSet = set([])

for _ in range(10):
    temp = int(input())
    tempSet.add(temp % 42)

print(len(tempSet))
