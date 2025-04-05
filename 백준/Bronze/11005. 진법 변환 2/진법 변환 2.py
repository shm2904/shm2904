import sys
input = sys.stdin.readline

a = list(input().rstrip().split())
b=int(a[0])
d=int(a[1])
c = list()

while(b!=0):
    c.append(b%d)
    e=b//d
    if b//d==0:
        break
    b=e
for i in c[::-1]:
    if i>=10:
        print(chr(i+55),end="")
    else:
        print(i,end="")
