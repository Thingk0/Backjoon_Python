
testCase = int(input())
avgList = []

for _ in range(testCase):
    student = list(map(int, input().split()))
    temp = student.pop(0)

    avg = sum(student) / len(student)

    avgCnt = 0
    for i in range(temp):
        avgCnt += 1 if student[i] > avg else 0

    str = f"{avgCnt / temp * 100:.3f}%"
    avgList.append(str)

for _ in avgList:
    print(_)
