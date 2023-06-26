import sys, os, io, atexit
from collections import deque
import copy
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

m, n, h = map(int, input().split())
#가로 세로 높이

arr = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
check_arr = [[[1 for _ in range(m)] for _ in range(n)] for _ in range(h)]
queue = deque()
for i in range(h):
    for j in range(n):
        arr[i][j] = list(map(int, input().split()))

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                queue.append([i, j, k])
            elif arr[i][j][k] == -1:
                check_arr[i][j][k] = -1    

if check_arr == arr:
    print(0)
else:
    answer = 0

    while queue:
        if check_arr == arr:
            break
        temp_queue = deque()
        while queue:
            ch, cn, cm = queue.popleft()
            for i in range(6):
                temp_h = ch + dz[i]
                temp_n = cn + dy[i]
                temp_m = cm + dx[i]
                if 0<= temp_h < h and 0<= temp_n < n and 0<=temp_m < m and arr[temp_h][temp_n][temp_m] == 0 :
                    arr[temp_h][temp_n][temp_m] = 1    
                    temp_queue.append([temp_h, temp_n, temp_m])  
        queue = copy.deepcopy(temp_queue)
        answer +=1

    if arr != check_arr:
        print(-1)
    else: 
        print(answer)