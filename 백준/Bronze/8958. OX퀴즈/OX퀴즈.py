import sys
input=sys.stdin.readline
N=int(input())
for k in range(N):
    a=list(input())
    i=0
    j=0
    for _ in range(len(a)):
        if a[_]=='O':
            i+=1
            j+=i
        elif a[_]=='X':
            i=0
    print(j)