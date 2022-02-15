

testCase = int(input())
case = list(input() for _  in range(testCase))
result = []

for ox in case:
    sum = 0
    increase = 1
    for j in ox:
        if j == 'O':
            sum += increase
            increase += 1
        else:
            increase = 1
    result.append(sum)

for i in result:
    print(i)