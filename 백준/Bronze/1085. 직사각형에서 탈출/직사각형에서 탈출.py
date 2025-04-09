import sys
import math
input = sys.stdin.readline

x,y,w,h = map(int,input().rstrip().split())
if 1<=w<=1000 and 1<=h<=1000 and 1<=x<=w-1 and 1<=y<=h-1:
    print(min(x,w-x,y,h-y))