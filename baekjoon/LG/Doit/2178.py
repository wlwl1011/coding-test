import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

arr = []
visited = [[0 for _ in range(M)]for _ in range(N)]
for _ in range(N):
    arr.append(list(map(int, input().rstrip())))

queue = deque()

queue.append((0,0,1))
answer = 0

while queue:
    x, y, l = queue.popleft()
    if x == N-1 and y == M-1:
        answer = l
        break

    for c in range(4):
        tx = x + dx[c]
        ty = y + dy[c]

        if 0 <= tx < N and 0 <= ty <M:
            if arr[tx][ty] and not visited[tx][ty]:
                visited[tx][ty] = True
                queue.append((tx,ty, l+1))

print(answer)