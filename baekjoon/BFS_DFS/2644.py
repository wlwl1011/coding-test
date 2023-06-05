import sys, os, io, atexit
from collections import deque
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def dfs(arr, v, visited):
    visited[v] = True

    for i in arr[v]:
        if not visited[i]:
            dfs(arr, i, visited )
            visited[i] = True


n = int(input())

v1, v2 = map(int,input().split())

m = int(input())

arr = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)

visited = [False] * n+1

for i in range(1, n+1):
    dfs(arr, i, v2, visited)