N=int(input())
if 4<=N<=1000 and N%4==0:
    i=0
    for i in range(N//4):
        i+=1
print("long "*i+"int")