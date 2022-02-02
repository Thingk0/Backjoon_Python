numList = []

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    numList.append(A+B)

for i in numList:
    print(i)
