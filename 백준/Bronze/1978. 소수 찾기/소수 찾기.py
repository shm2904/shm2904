import sys
import math
input = sys.stdin.readline

A = int(input().rstrip())
B = list(map(int, input().rstrip().split())) 
C=[]
for i in B:
    if i > 1:
        for j in range(2, int(math.sqrt(i)) + 1): 
            if i % j == 0:                  break
        else:  
            C.append(i)
print(len(C))
