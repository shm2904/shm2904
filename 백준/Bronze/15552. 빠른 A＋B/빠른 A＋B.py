import sys

T=int(sys.stdin.readline())
a_arr=[]
b_arr=[]
for i in range(T):
    a,b=map(int, sys.stdin.readline().split())
    a_arr.append(a)
    b_arr.append(b)
for i in range(T):
    print(a_arr[i]+b_arr[i])