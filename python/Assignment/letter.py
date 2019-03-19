print('Enter a string')
s = input()
d = dict()

for i in s:
    if (i not in d):
        d[i] = 1
    else:
        d[i] = d[i] + 1
print(d)
