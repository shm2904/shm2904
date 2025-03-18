X=int(input())
N=int(input())
list_a=[]
list_b=[]
1<=X<=1000000000
1<=N<=100
for i in range(N):
    a,b=map(int,input().split())
    if 1<=a<=1000000 and 1<=b<=10:
        list_a.append(a)
        list_b.append(b)
c=0
for i in range(N):
    d=list_a[i]*list_b[i]
    c+=d
if X==c:
    print("Yes")
else:
    print("No")