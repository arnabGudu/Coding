def conv(n, b, t):
    sum = 0
    i = 0
    while (n > 0):
        sum += (n % t) * (b ** i)
        n /= t
        i = i + 1
    return sum

print('Enter a base')
b = input()
print('Enter a no of the selected base')
n = input()

if (b == 2):
    print('dec:')
    print(conv(n, b, 10))
    print('bin:')
    print(conv(n, b, 16))

elif (b == 10):
    print(conv(n, b, 2))
    print(conv(n, b, 16))

elif (b == 16):
    print(conv(n, b, 2))
    print(conv(n, b, 10))
