selfNum = [ 0 for i in range(10000) ]


def d(number):
    sum = number
    while number != 0:
        sum += number % 10
        number //= 10

    return sum


for i in range(1, 100001):
    temp = d(i)
    selfNum[temp] = 1


for i in range(1, 100001):
    if selfNum[i] == 0:
        print(i)



