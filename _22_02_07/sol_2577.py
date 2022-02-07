
A = int(input())
B = int(input())
C = int(input())
result = str(A*B*C)

num = [ 0 for i in range(10) ]

for i in result:
    idx = int(i)
    num[idx] += 1

for n in num:
    print(n)