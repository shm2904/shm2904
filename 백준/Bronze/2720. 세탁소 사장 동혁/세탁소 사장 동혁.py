import sys
input = sys.stdin.readline

a = int(input().rstrip())
quarter=list()
dime=list()
nickel=list()
penny=list()
for i in range(a):
    b=int(input())
    quarter.append(b//25)
    dime.append((b%25)//10)
    nickel.append((b%25%10)//5)
    penny.append(b%25%10%5)
for i in range(a):
    print(quarter[i],dime[i],nickel[i],penny[i])