import sys
import math
input = sys.stdin.readline

A = int(input().rstrip())
B=[]

c=2
while c*c<=A:
    while A%c==0:
        B.append(c)
        A=A//c
    c+=1
if A>1:
    B.append(A)
B.sort()
for i in B:
    print(i)