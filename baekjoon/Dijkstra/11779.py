import heapq
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

INF = int(1e9)

n = int(input())
m = int(input())

graph = [ [] for _ in range(n+1)]

distance = [INF] * (n+1)

for i in range(m):
    start, end, value = map(int, input().split())
    graph[start].append((end, value))

start, end = map(int, input().split())

def dijkstra(start):
    q = [] 
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여 queue에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
  
    while q: #큐가 비어있지 않다면
        #가장 최단 거리가 짧은 노드에 대한 정보 끝내기
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist+ i[1]
            #현재 노드를 거쳐서 다른 노드를 이동하는게 더 짧은 경우
            if cost < distance[i[0]]:

                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start, end)           

print(distance[end])

for i in answer:
    print(i, end = " ")