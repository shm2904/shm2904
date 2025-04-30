import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = []
for i in range(N):
    a.append(input().strip())

c = 64

for i in range(N - 7):  
    for j in range(M - 7):
        c1 = 0
        c2 = 0

        for x in range(8):
            for y in range(8):
                d = a[i + x][j + y]
                if (x + y) % 2 == 0:
                    if d != 'W':
                        c1 += 1
                    if d != 'B':
                        c2 += 1
                else:
                    if d != 'B':
                        c1 += 1
                    if d != 'W':
                        c2 += 1

        c = min(c, c1, c2)

print(c)
