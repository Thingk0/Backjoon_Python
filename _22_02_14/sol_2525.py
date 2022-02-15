
hour, minute = map(int, input().split())
timer = int(input())

print(((hour + (minute + timer) // 60) % 24), (minute+timer) % 60)