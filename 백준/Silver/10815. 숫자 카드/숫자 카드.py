import sys
input=sys.stdin.readline

N = int(input())
a = set(input().split()) 
K = int(input())
b = input().split()

for x in b:
    if x in a:
        print(1,end=' ')
    else:
        print(0, end=' ')