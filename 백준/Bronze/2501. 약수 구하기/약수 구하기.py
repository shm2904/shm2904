import sys
input = sys.stdin.readline

C = []

A, B = map(int, input().rstrip().split())

for i in range(1, A + 1):
    if A % i == 0:
        C.append(i)

C.sort() 

if B <= len(C):
    print(C[B - 1])
else:
    print(0)
