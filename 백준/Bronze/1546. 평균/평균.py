import sys
input=sys.stdin.readline

A=int(input())
B=list(map(int,input().split()))
n=(sum(B)/max(B)*100)/A
print(n)