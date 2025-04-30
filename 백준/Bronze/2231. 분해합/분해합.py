import sys
input = sys.stdin.readline

N = int(input())
b = N

for i in range(N):
    a = list(map(int, list(str(i))))
    c = sum(a)
    d = c + i
    if d == N:
        b = min(b, i)
        break

if b == N:
    print(0)
else:
    print(b)
