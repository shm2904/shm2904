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
        print(0,end=" ")
    else:
        if a[bisect_left(a,i)]==i:
            print(bisect_right(a,i)-bisect_left(a,i),end=" ")
        else:
            print(0,end=" ")