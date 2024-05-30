import sys
input = sys.stdin.readline
import heapq

N = int(input())

hq = []
hq2 = []
for _ in range(N):
    ip = int(input().rstrip())
    if ip > 0:
        heapq.heappush(hq, -(ip))
    else:
        heapq.heappush(hq2, ip)

answer = 0

while hq:
    a, b = 0,0
    if hq:
        a = -(heapq.heappop(hq))
    else:
        
        break
    if hq:
        b = -(heapq.heappop(hq))
    else:
        answer +=  a
        break
    if a + b < a*b:
        answer += (a*b)
    else:
        answer += (a+b)

answer2 = 0

while hq2:
    a, b = 0,0
    if hq2:
        a = heapq.heappop(hq2)
    else:
        
        break
    if hq2:
        b = heapq.heappop(hq2)
    else:
        answer2 +=  a
        break
    if a + b < a*b:
        answer2 += (a*b)
    else:
        answer2 += (a+b)

print(answer+answer2)


