# import sys, os, io, atexit
# input = lambda: sys.stdin.readline().rstrip('\r\n')
# stdout = io.BytesIO()
# sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
# atexit.register(lambda: os.write(1, stdout.getvalue()))
from collections import deque

queue = deque()

N = int(input())
arr = [ [0 for _ in range(N)] for _ in range(N)]
visited = [ [0 for _ in range(N)] for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

dictionary ={}

for i in range(N):
    arr[i] = list(map(int, input()))
    for j in range(N):
        if arr[i][j] == 1:
            dictionary[(i,j)] = 1
            

cnt = 1
cnt_count = [0 for _ in range(N*N)]
queue = deque()

for index_i, index_j in dictionary.keys():
    
    
    if visited[index_i][index_i]: #방문 안 한곳만 !
        continue
    print(index_i,index_j)
    for i in range(N):
        print(arr[i])
    for i in range(N):
        print(visited[i])
    queue.append((index_i, index_j))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < N and 0 <= ty < N : #범위 내의 값
                if not visited[tx][ty]:
                    if arr[tx][ty]: #벽이면
                        visited[tx][ty] = cnt
                        cnt_count[cnt] += 1 ##cnt 개수 기록
                        queue.append((tx,ty))    
    cnt += 1                  
                

print(cnt)
cnt_count.sort()
for i in range(cnt):
    if cnt_count[i] != 0:
        print(cnt_count[i])
