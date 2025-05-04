import sys
import heapq

input = sys.stdin.readline

N = int(input())
a = []

for _ in range(N):
    heapq.heappush(a, int(input()))

b = 0

while len(a) > 1:
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    c = x + y
    b += c
    heapq.heappush(a, c)

print(b)
