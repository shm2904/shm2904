import sys

T=int(input())
a_arr=[]
b_arr=[]
for i in range(T):
    a,b=map(int, sys.stdin.readline().split())
    if 0<a<10 and 0<b<10:
        a_arr.append(a)
        b_arr.append(b)
for i in range(T):
    print("Case #%d: %d + %d = %d"%(i+1,a_arr[i],b_arr[i],a_arr[i]+b_arr[i]))
