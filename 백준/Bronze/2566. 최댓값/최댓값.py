import sys
input = sys.stdin.readline

try:
    C = []
    for i in range(9):
        c = list(map(int, input().split()))
        C.append(c)

    d = 0
    a = 0
    b = 0

    for i in range(9):
        for j in range(9):
            if d < C[i][j]:
                d = C[i][j]
                a = i
                b = j

    print(d)
    print(a + 1, b + 1)

except:
    print(0)