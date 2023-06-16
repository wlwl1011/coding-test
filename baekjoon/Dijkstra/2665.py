import heapq
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int, input()))

visited = [ [0] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dijkstra():
    heap = []
    heapq.heappush(heap, [0,0,0])
    visited[0][0] = 1

    while heap:
        cost, x, y = heapq.heappop(heap)
        if x == n-1 and y == n-1:
            return cost
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if arr[nx][ny] == 0:
                    heapq.heappush(heap,[cost + 1 , nx, ny])
                else:
                    heapq.heappush(heap, [cost, nx, ny])


print(dijkstra())