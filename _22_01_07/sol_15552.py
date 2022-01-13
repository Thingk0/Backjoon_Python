import sys

TestCase = int(input())

for i in range(TestCase):
    A,B = map(int, sys.stdin.readline().split())
    print(A+B)