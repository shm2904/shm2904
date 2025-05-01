import sys
input = sys.stdin.readline

N = int(input().rstrip())
a=[]
for i in range(N):
    a.append((int(input()),i))
a.sort()
c=0

for i in range(N):
    d=a[i][1]-i
    if d>c:
        c=d
     
print(c+1)