import sys
input = sys.stdin.readline

a = int(input().rstrip())
c=2
for i in range(a):
    c=c+(c-1)
print(c*c)
