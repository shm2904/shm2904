import sys
input = sys.stdin.readline

A = int(input())
a = []
for i in range(100):
    a.append([0] * 100)
for i in range(A):
    b, c = map(int, input().split())
    for j in range(b, b + 10):
        for k in range(c, c + 10):
            a[j][k] = 1
d = 0
for j in a:
    d += j.count(1)
print(d)
