import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    weight[start] = 0

    while hq:
        node_weight, node = heapq.heappop(hq)
        if weight[node] < node_weight:
            continue

        for v, w in graph[node]:
            tw = node_weight + w
            if weight[v] > tw:
                weight[v] = tw
                heapq.heappush(hq, (tw, v))

N = int(input())
M = int(input())

weight = [int(1e9)] * N
graph = [[] for _ in range(N)]

for _ in range(M):
    u, v, w = map(int, input().rstrip().split())
    u -= 1
    v -= 1
    graph[u].append((v, w))

start, end = map(int, input().split())
start -= 1
end -= 1

dijkstra(start)
print(weight[end])
