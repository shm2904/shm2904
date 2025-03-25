import sys
input=sys.stdin.readline

a,b=map(int, input().split())
c=map(int,input().split())
for x in c:
    if x<b:
        print(x,end=' ')