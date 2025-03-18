A,B=map(int,input().split())
C=int(input())
if 0<=A<=23 and 0<=B<=59 and 0<=C<=1000:
    D=B+C
    if D>59:
        if A+(D//60)<24:
            print(A+(D//60), D%60)
        else:
            print(A+(D//60)-24, D%60)
    else:
        print(A, D)