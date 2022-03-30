
def hanNum(X):
    if 0 < X < 100:
        result = X
        return result

    else:
        result = 99
        for i in range(100, X+1):
            tempList = []
            tempNum = i

            if i == 1000:
                result -= 1

            while tempNum > 0:
                tempList.append(tempNum % 10)
                tempNum //= 10

            if tempList[0] - tempList[1] == tempList[1] - tempList[2]:
                result += 1

        return result


X = int(input())
print(hanNum(X))
