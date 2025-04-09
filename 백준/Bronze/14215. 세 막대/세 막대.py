import sys
input = sys.stdin.readline

a = list(map(int,input().rstrip().split()))
a.sort()
if a[2]<a[0]+a[1]:
    print(sum(a))
else:
    a[2]=a[1]+a[0]-1
    print(sum(a))