import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    weight[start][0] = 0

    while hq:
        node_weight, node = heapq.heappop(hq)
        
        # 현재 노드의 경로들이 K개 채워져 있는지 확인
        for v, w in graph[node]:
            tw = node_weight + w
            if weight[v][K-1] > tw:
                weight[v][K-1] = tw
                weight[v].sort()  # 이 부분을 효율적으로 바꾸기
                heapq.heappush(hq, (tw, v))

N, M, K = map(int, input().rstrip().split())

weight = [[int(1e9)] * K for _ in range(N)]
graph = [[] for _ in range(N)]

for _ in range(M):
    u, v, w = map(int, input().rstrip().split())
    u -= 1
    v -= 1
    graph[u].append((v, w))

dijkstra(0)

for i in range(N):
    if weight[i][K-1] == int(1e9):
        print(-1)
    else:
        print(weight[i][K-1])
