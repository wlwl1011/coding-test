import sys
import heapq
input = sys.stdin.readline

N = int(input())
hq = []

for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(hq, (abs(x),x))
    else:
        if hq:
            abs_x, x = heapq.heappop(hq)
            print(x)
        else:
            print(0)