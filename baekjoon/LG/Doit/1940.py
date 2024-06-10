import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
M = int(input())

arr = list(map(int, input().split()))
cnt = 0

arr.sort()

start = 0
end = N-1

while start < end:
    if arr[start] + arr[end] <= M:
        if arr[start] + arr[end] == M:
            cnt += 1
        start += 1
    else:
        end -= 1
        
print(cnt)