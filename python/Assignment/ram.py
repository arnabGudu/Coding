from __future__ import print_function

s = input()

lastSpace = -1

p = ''

for i in range(0, len(s)):
    if (s[i] == ' '):
        for j in range(i - 1, lastSpace, -1):
            p += s[j]
        lastSpace = i
        p += ' '

    elif (i == len(s) - 1):
        for j in range(i, lastSpace, -1):
            p += s[j]
print(p)


