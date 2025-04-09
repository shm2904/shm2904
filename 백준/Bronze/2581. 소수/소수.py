import sys
import math
input = sys.stdin.readline

A = int(input().rstrip())
B = int(input().rstrip()) 
C = []

for i in range(A, B + 1):
    if i > 1:
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            C.append(i)
if len(C) == 0:
    print(-1)
else:
    print(sum(C))
    print(min(C))
