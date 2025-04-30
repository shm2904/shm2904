import sys
input = sys.stdin.readline

N, M = map(int, input().split())
L = list(map(int, input().split()))
b=0

for i in range(N):
    for j in range(i+1, N):
        for c in range(j+1, N):
            a = L[i] + L[j] + L[c]
            if a <= M:
                b = max(b, a)

print(b)
