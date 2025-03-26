import sys
input=sys.stdin.readline

a=[]
for i in range(1,31):
    a.append(i)
for j in range(28):
    b=int(input())
    a.remove(b)
print(min(a))
print(max(a))