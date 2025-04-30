import sys
input = sys.stdin.readline

N = int(input().strip())

a = []
b = 666

while True:
    if '666' in str(b):
        a.append(b)
        if len(a) == N:
            print(a[N-1])
            break
    b += 1
