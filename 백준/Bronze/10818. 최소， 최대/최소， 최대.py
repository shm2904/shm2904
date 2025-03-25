import sys
input=sys.stdin.readline

N=int(input())
a=list(map(int,input().split()))
b=max(a)
c=min(a)
print(min(a),max(a))