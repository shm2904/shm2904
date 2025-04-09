import sys
input = sys.stdin.readline

a = int(input().rstrip())

if a == 1:
    print(1)
else:
    b = 1
    while a > 1:
        a -= 6 * b
        b += 1 
    print(b) 
