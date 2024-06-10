import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

arr = deque([i for i in range(N,0,-1)])

while len(arr) > 1:
    if arr:
        arr.pop()
    if arr:
        tmp = arr.pop()
        arr.appendleft(tmp)


print(arr[-1])
