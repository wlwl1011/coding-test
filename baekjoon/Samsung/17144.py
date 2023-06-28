import sys, os, io, atexit
import copy
from collections import deque
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

r, c, t = map(int, input().split())

arr = [[0 for _ in range(c)] for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cleaner = []
for i in range(r):
    arr[i] = list(map(int, input().split()))
    if arr[i][0] == -1:
        cleaner.append([i,0])
    
temp_arr = copy.deepcopy(arr)

while t>0:
    #먼지 확산
    queue = deque()
    queue.append([0,0])
    visited = [[0 for _ in range(c)] for _ in range(r)]
    while queue:
        tr, tc = queue.popleft()
        dust = temp_arr[tr][tc]
        if visited[tr][tc] == 1:
            continue
        visited[tr][tc] = 1
        for i in range(4):
            cr = tr+dx[i]
            cc = tc+dy[i]
            if 0 <= cr < r and 0 <= cc < c:
                if visited[cr][cc] == 0:
                    queue.append([cr, cc])
                if dust == 0:
                    continue
                if dust == -1:
                    continue
                if temp_arr[cr][cc] == -1:
                    continue
                    #확산 시키는 칸에 먼지가 있으면
                    #확산 시키는 칸이 공기 청정기가 아니면
                    #확산될 칸이 공기 청정기가 아니면
                arr[cr][cc] = arr[cr][cc] + dust//5 
                arr[tr][tc] -= dust//5

           
        if tr == r-1 and tc == c-1:
            break

          
    temp_arr = copy.deepcopy(arr)            
    # cleaner[0] 반시계 방향으로 이동 
    for i in range(0,cleaner[0][0]+1): 
        for j in range(c):
            if [i,j] in cleaner:
                continue
            if i == 0: # 위쪽 외곽
                if j == 0: # 0 번째 열 처리
                    arr[i+1][j] = temp_arr[i][j]        
                elif j == c-1: # 맨 끝 열 처리
                    arr[i][j] = temp_arr[i+1][j]
                else:
                    arr[i][j] = temp_arr[i][j+1] 
            elif i == cleaner[0][0]: # 가장 아랫쪽 외곽
                if j == c-1: # 맨 끝 열 처리
                    arr[i-1][j] = temp_arr[i][j]
                    arr[i][j] = temp_arr[i][j-1]
                elif j == 0:
                    continue    
                else:
                    if temp_arr[i][j-1] == -1:
                        arr[i][j] = 0
                    else:    
                        arr[i][j] = temp_arr[i][j-1] 
            else: # 그를 제외한 나머지 행은 0번째와 r-1 번째만 처리해준다.
                if j == 0: # 0 번째 열 처리
                    if arr[i][j] != -1:
                        arr[i][j] = temp_arr[i-1][j]
                elif j == c-1: # 맨 끝 열 처리
                    arr[i-1][j] = temp_arr[i][j]

    
    # cleaner[1] 시계 방향으로 이동 
    for i in range(cleaner[1][0], r): 
        for j in range(c):
            if [i,j] in cleaner:
                continue
            if i == cleaner[1][0]: # 위쪽 외곽
                if j == 1: # 0 번째 열 처리
                    arr[i][j] = 0
                elif j == c-1: #r-1 처리
                    arr[i+1][j] = temp_arr[i][j]   
                    arr[i][j] = temp_arr[i][j-1] 
                else: #그외
                    arr[i][j] = temp_arr[i][j-1]        
                
            elif i == r-1: # 가장 아랫쪽 외곽
                if j == c-1: # 맨 끝 열 처리
                    arr[i][j] = temp_arr[i-1][j]
                elif j == 0:
                    arr[i-1][j] = temp_arr[i][j]  
                    arr[i][j] = temp_arr[i][j+1]
                else:
                    arr[i][j] = temp_arr[i][j+1] 
            else: # 그를 제외한 나머지 행은 0번째와 r-1 번째만 처리해준다.
                if j == 0: # 0 번째 열 처리
                    if arr[i][j] != -1:
                        arr[i][j] = temp_arr[i+1][j]
                elif j == c-1: # 맨 끝 열 처리
                    arr[i][j] = temp_arr[i-1][j]
    
    temp_arr = copy.deepcopy(arr)    
    t -= 1

sum = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] != -1:
            sum += arr[i][j]

print(sum)

             



    
