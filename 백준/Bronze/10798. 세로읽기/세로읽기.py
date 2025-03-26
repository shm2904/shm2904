import sys
input = sys.stdin.readline

A = list(input().strip())
B = list(input().strip())
C = list(input().strip())
D = list(input().strip())
E = list(input().strip())

F = [A, B, C, D, E]

a=max(map(len,F))
for i in range(a):
    for j in F:
        if i<len(j):
            print(j[i],end="")