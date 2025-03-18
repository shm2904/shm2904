a=input()
b=input()
c=0
d=0
f=0
list_a=list(map(int,a))
list_b=list(map(int,b))
for i in range(3):
    c+=list_b[2]*(list_a[2-i]*(10**i))
for i in range(3):
    d+=list_b[1]*(list_a[2-i]*(10**i))
for i in range(3):
    f+=list_b[0]*(list_a[2-i]*(10**i))
print(c)
print(d)
print(f)
print(c+d*10+f*100)