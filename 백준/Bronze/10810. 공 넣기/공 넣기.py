N,M=map(int,input().split())
d=[0]*N
for i in range(M):
    a,b,c=map(int, input().split())
    for i in range(a-1,b):
        d[i]=c
for j in d:
    print(j, end=" ")