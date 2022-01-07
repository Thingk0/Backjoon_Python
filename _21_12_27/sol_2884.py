
hour, minute = map(int, input().split())

if 0 <= hour <= 23 and 0 <= minute <= 59:
    if hour >= 1 and minute < 45: # 1시 이상일 때
        hour -= 1
        minute += 15
    elif minute < 45: # 0시 일 때
        hour += 23
        minute += 15
    else:
        minute -= 45 # 45분 이상일 때

print(hour,minute)