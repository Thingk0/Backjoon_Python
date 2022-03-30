alphabetList = [-1] * 26
strings = input()

for (index, string) in enumerate(strings):
    if alphabetList[ord(string)-97] == -1:
        alphabetList[ord(string) - 97] = index

for i in alphabetList:
    print(i, end=' ')