print('no of instructions')
i = input()
d = {'FORWARD':0, 'BACKWARD':0, 'LEFT':0, 'RIGHT':0}

for i in range(0, i):
    j = input().split(' ')
    d[j[0]] = d[j[0]] + int(j[1])


y = d['FORWARD'] - d['BACKWARD']
x = d['RIGHT'] - d['LEFT']

disp = (x * x + y * y)**.5
print(d)
print('displacement : ')
print(disp)

