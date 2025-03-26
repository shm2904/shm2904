import sys
input=sys.stdin.readline

N,M=map(int,input().split())
d=[0]*N
c=0
for i in range(N):
    d[i]=i+1
for j in range(M):
    a,b=map(int,input().split())
    c=d[a-1]
    d[a-1]=d[b-1]
    d[b-1]=c
for j in d:
    print(j, end=" ")
