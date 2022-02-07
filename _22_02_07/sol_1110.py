N = int(input())
cntCycle = 0


def addCycle(num):
    num = ((num % 10) * 10) + (((num // 10) + (num % 10)) % 10)
    return num


tempN = addCycle(N)
cntCycle += 1

while tempN != N:
    tempN = addCycle(tempN)
    cntCycle += 1

print(cntCycle)
