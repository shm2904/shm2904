N=int(input())
if 1<=N<=100:
    for i in range(N):
        i+=1
        print(' '*(N-i)+'*'*i)
