A = int(input())
B = input()

for i in range(len(B), 0, -1):
    print(A * int(B[i-1]))

print(A * int(B))


"""
num1 = int(input())
num2 = int(input())

print(num1 * (num2%10))
print(num1 * ((num2%100)//10))
print(num1 * (num2//100))
print(num1 * num2)
"""

"""
num1 = int(input())
num2 = input()

for i in range(len(num2), 0, -1):
    print(num1 * int(num2[i-1]))

print(num1 * int(num2))
"""

"""
num1 = int(input())
num2 = list(map(int, input()))

result = []

for i in range(len(num2), 0, -1):
  result.append(num1 * num2[i-1])

print(result[0], result[1], result[2], sep='\n')
print(result[0]+(result[1]*10)+result[2]*100)
"""