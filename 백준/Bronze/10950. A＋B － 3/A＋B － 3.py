T=int(input())
list_A=[]
list_B=[]
for i in range(T):
    A,B=map(int, input().split())
    list_A.append(A)
    list_B.append(B)
for i in range(T):
    print(list_A[i]+list_B[i])