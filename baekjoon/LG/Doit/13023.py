import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def dfs(n, depth):
    
    global flag

    if flag:
        return
    if depth >= 4:
        flag = True
        return
    
    for i in graph[n]:
        if not visited[i]:
            visited[i] = True
            dfs(i,depth + 1)
            visited[i] = False

N, M = map(int, input().split())
graph = [[] for _ in range(N)]


for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

global flag
flag = False

for i in range(N):
    visited = [False for _ in range(N)]
    visited[i] = True
    dfs(i,0)
    if flag:
        break

if flag:
    print(1)
else:
    print(0)



