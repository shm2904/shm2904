import sys
input=sys.stdin.readline

N,M=map(int,input().split())
b=[]
d=[]
for i in range(N):
    b.append(i+1)
for j in range(M):
    a,c=map(int,input().split())
    d=b[a-1:c]
    d.reverse()
    b[a-1:c]=d
for k in b:
    print(k,end=" ")