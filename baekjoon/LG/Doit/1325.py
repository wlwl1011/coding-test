import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True
    count = 1
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

result = []
max_count = 0

for i in range(1, N + 1):
    count = bfs(i)
    if count > max_count:
        max_count = count
        result = [i]
    elif count == max_count:
        result.append(i)

print(' '.join(map(str, sorted(result))))
