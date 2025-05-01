import sys
input = sys.stdin.readline

N = int(input().rstrip())

e=list(map(int,input().rstrip().split()))
e.sort(reverse=1)
if len(e)%2==0:
    print(e[len(e)//2])
else:
    print(e[(len(e)-1)//2])