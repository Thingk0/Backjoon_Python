
num = int(input())
star_num = 1

for i in range(num,0,-1):
    print((" " * (i-1)) + ("*" * star_num))
    star_num += 1