a_arr=[]
b_arr=[]

while(True):
    a,b=map(int, input().split())
    if a==0 and b==0:
        break
    if 0<a<10 and 0<b<10:
        a_arr.append(a)
        b_arr.append(b)
for i in range(len(a_arr)):
    print(a_arr[i]+b_arr[i])