import sys
input = sys.stdin.readline
a, b = map(int, input().split())
A = []
B = []
for i in range(a):
    c = list(map(int, input().split()))
    A.append(c)
for i in range(a):
    c = list(map(int, input().split()))
    B.append(c)
for i in range(a):
    C = []
    for j in range(b):
        C.append(A[i][j] + B[i][j])
    print(*C)
