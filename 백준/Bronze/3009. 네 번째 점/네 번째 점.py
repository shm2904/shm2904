import sys
import math
input = sys.stdin.readline
a=[]
b=[]
for i in range(3):
    x,y= map(int,input().rstrip().split())
    a.append(x)
    b.append(y)
if a.count(a[0])==1:
    c=a[0]
elif a.count(a[1])==1:
    c=a[1]
elif a.count(a[2])==1:
    c=a[2]

if b.count(b[0])==1:
    d=b[0]
elif b.count(b[1])==1:
    d=b[1]
elif b.count(b[2])==1:
    d=b[2]

print(c,d)