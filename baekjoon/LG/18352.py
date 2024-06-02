import sys
input = sys.stdin.readline
from collections import deque
N, M, K, X = map(int, input().rstrip().split())

graph = [[] for _ in range(N)]
distance = [int(1e9) for _ in range(N)]

distance[X-1] = 0

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    a -=1
    b -=1

    graph[a].append(b)

for a in graph[X-1]:
    queue = deque()
    queue.append((a,0))
    while queue:
        node, depth = queue.popleft()
        if distance[node] > depth + 1:
            distance[node] = depth + 1
        for n in graph[node]:
            if distance[n] > depth + 1:
                queue.append((n, depth+1))

flag = False
# print(distance)
for i in range(N):
    if distance[i] == K:
        flag = True
        print(i+1)

if not flag:
    print(-1)
