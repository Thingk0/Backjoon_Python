import sys

input()
num = [int(n) for n in sys.stdin.readline().split()]

print(min(num), max(num))