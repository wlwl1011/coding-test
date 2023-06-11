import sys, os, io, atexit
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque
import copy
n, m = map(int, input().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_graph[nx][ny] == 0: 
                tmp_graph[nx][ny] = 2 
                queue.append((nx, ny)) 

    global answer
    cnt = 0

    for i in range(n):
        cnt += tmp_graph[i].count(0)

    answer = max(answer, cnt)

def makeWall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0: # 빈 공간이라면 벽 세우기 가능
                graph[i][j] = 1 # 벽을 세우고
                makeWall(cnt+1) # 다시 두번째 벽 세우러 간다
                graph[i][j] = 0 # 다시 벽을 허무는 과정 (백트래킹)

for i in range(n):
    graph.append(list(map(int, input().split())))
answer = 0
makeWall(0)
print(answer)