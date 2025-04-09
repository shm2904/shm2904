import sys
input = sys.stdin.readline

A,B,V = map(int,input().rstrip().split())
a=0
if V<=A:
    print(1)
else:
    a+=V-A
    b=(a+(A-B)-1)//(A-B)+1
    print(b)