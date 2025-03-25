import sys
input=sys.stdin.readline

N=int(input())
a=map(int,input().split())
b=int(input())
i=0
for x in a:
    if x==b:
        i=i+1
print(i)