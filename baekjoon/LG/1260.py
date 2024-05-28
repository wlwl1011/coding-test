import sys
input = sys.stdin.readline
from collections import deque

def dfs(n):
    print(n+1,end=" ")
    visited_dfs[n] = True

    for i in graph[n]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(n):
    queue = deque()
    visited = [False for _ in range(N)]
    visited[n]= True
    queue.append(n)
    while(queue):
        x = queue.popleft()
        print(x+1, end=" ")
        for i in graph[x]:
            if not visited[i]:
                visited[i]= True
                queue.append(i)
        
N, M, V = map(int, input().split())
visited_dfs = [False for _ in range(N)] 
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for i in range(N):
    graph[i].sort()


dfs(V-1)
print()
bfs(V-1)