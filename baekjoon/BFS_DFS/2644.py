import sys, os, io, atexit
from collections import deque
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

global depth
global flag
def dfs(arr, v1, v2, visited):
    global depth
    global flag
    #print(v1, v2)
    visited[v1] = True
    check_list = arr[v1]
    depth += 1

    for i in check_list:
        if not visited[i]:
            #print(v1, check_list, "i : ", i)
            if i == v2:
                flag = depth
                return
            dfs(arr, i, v2, visited)
            visited[i] = True
            

n = int(input())

v1, v2 = map(int,input().split())

m = int(input())

arr = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

#print(arr)

visited = [False] * (n+1)

depth = 0
flag = 0
dfs(arr, v1, v2, visited)
if flag:
    print(flag)
else:
    print(-1)    