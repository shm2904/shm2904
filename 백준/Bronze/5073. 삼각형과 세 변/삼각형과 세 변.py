import sys
input = sys.stdin.readline

while True:
    a = list(map(int,input().rstrip().split()))
    a.sort()
    if a[0]==a[2]==a[1]==0:
        break
    if a[2]<a[0]+a[1]:
        if a[0]==a[2]==a[1]:
            print("Equilateral")
        elif a[0]==a[1] or a[0]==a[2] or a[1]==a[2]:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")