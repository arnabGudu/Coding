print('Enter no of entries')
n = input()
d = dict()

for i in range(0, n):
    s = input().split(' ')
    d[s[0]] = int(s[1])

print('sort by ??')

q = input()

if (q == 'name'):
   for i in sorted(d.keys()):
       print("{0} : {1}".format(i, d[i]))

elif (q == 'age'):
    for i in sorted(d.values()):
        for j in d.keys():
            if (d[j] == i):
                print("{0} : {1}".format(j, i))

