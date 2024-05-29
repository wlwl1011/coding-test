import sys
import heapq
input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    arr.append(int(input().rstrip()))

if N == 1:
    print(0)
elif N == 2:
    print(sum(arr))
else:   
    answer = 0
    heapq.heapify(arr)
    while len(arr) > 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        answer += a + b
        # print(a,b)

        heapq.heappush(arr,a+b)
    print(answer)

