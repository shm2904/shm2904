import sys
input = sys.stdin.readline

a = list(input().rstrip().split())
b = int(a[1])
c = 0

if a[0].isnumeric() == True:
    for i, j in enumerate(a[0]):
        c = c + (int(j) * (b ** (len(a[0]) - i - 1)))
else:
    for i, j in enumerate(a[0]):
        if '0' <= j <= '9':
            d = int(j)
        else:
            d = ord(j) - 55
        c = c + (d * (b ** (len(a[0]) - i - 1)))

print(c)
