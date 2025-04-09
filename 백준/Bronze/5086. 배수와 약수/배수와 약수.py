import sys
input = sys.stdin.readline

C=list()

while True:
    A,B=map(int,input().rstrip().split())
    if A==0 and B==0:
        break
    if A>B and A%B==0:
        C.append("multiple")
    elif A<B and B%A==0:
        C.append("factor")
    else:
        C.append("neither")
for i in C:
    print(i)