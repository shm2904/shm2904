import sys
input=sys.stdin.readline

from bisect import bisect_left, bisect_right

N=int(input())
a=list(map(int, input().rstrip().split()))
M=int(input())
b=list(map(int, input().rstrip().split()))

a.sort()

for i in b:
    if bisect_left(a,i)==N:
        print(0)
    else:
        if a[bisect_left(a,i)]==i:
            print(1)
        else:
            print(0)