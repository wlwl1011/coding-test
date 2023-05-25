import sys, os, io, atexit
from collections import deque
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def dfs(graph,v,visited):
    
    #방문 노드 처리
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph,start,visited):    
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    v1, v2 = map(int , input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

#print(graph)

for i in range(n+1):
    graph[i].sort()

visited = [False] * (n+1)
print_list = []
dfs(graph, v, visited) 
print()
visited = [False] * (n+1)
bfs(graph, v, visited)
