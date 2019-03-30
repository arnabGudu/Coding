def binDec(n, b, t):
    sum = 0
    i = 0
    while (n > 0):
        sum += (n % t) * (b ** i)
        n /= t
        i = i + 1
    return sum

def decToHex(n):
    sum = ''
    while (n > 0):
        rem = n % 16
        if (rem >= 10):
            alpha = ['A','B','C','D','E','F']
            sum += alpha[rem - 10]
        else:
            sum += str(rem)
        n /= 16
        
        out = ''
        for i in range(len(sum) - 1, -1, -1):
            out += sum[i]

    return out

def hexToDec(n):
    c = 0
    sum = 0
    for i in range(len(n) - 1, -1, -1):
        alpha = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
        
        if (n[i] in alpha.keys()):
                sum += alpha[n[i]] * 16 ** c
        else:
            sum += int(n[i]) * 16 ** c
        c = c + 1
    return sum
         
print('Enter a base')
b = input()
print('Enter a no of the selected base')
n = input()

if (b == 2):
    print('dec:')
    dec = binDec(n, b, 10)
    print(dec)
    print('hex:')
    print(decToHex(dec))

elif (b == 10):
    print('bin:')
    print(binDec(n, b, 2))
    print('hex:')
    print(decToHex(n))

elif (b == 16):
    print('bin:')
    print(binDec(hexToDec(n), 10, 2))
    print('dec:')
    print(hexToDec(n))
