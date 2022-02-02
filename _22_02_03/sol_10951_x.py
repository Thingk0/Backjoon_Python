numList = []

while True:
    try:
        A, B = map(int, input().split())
        numList.append(A+B)
    except:
        break

for i in numList:
    print(i)