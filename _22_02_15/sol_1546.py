
times = int(input())
sum = 0
scores = list(map(float, input().split()))
maxNum = max(scores)

for i in scores:
    sum += (i / maxNum) * 100

print(sum / times)