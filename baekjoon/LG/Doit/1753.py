import sys
from collections import deque
input = sys.stdin.readline
import heapq

def dijkstra(start):
    queue = []
    heapq.heappush(queue,(0,start))

    while queue:
        node_weight, node = heapq.heappop(queue)

        for a,w in graph[node]:
            tw = node_weight + w
            if tw < weight[a]:
                weight[a] = tw
                heapq.heappush(queue,(tw,a))


V, E = map(int, input().rstrip().split())

graph = [[] for _ in range(V)]
weight = [int(1e9) for _ in range(V)]

start = int(input().rstrip())
start -= 1
weight[start] = 0

for _ in range(E):
    u,v,w = map(int, input().rstrip().split())
    u -= 1
    v -= 1
    graph[u].append((v,w))

dijkstra(start)

for i in range(V):
    if weight[i] == int(1e9):
        print("INF")
    else:
        print(weight[i])


