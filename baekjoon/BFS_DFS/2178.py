import sys, os, io, atexit
from collections import deque
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m = map(int,input().split())
arr = []

for i in range(n):
    temp = list(map(int,input()))
    arr.append(temp)

#print(arr)

dx = [-1, 1, 0, 0]  
dy = [0, 0, -1, 1]


check_list = deque()
check_list.append([0,0])

while check_list:
    x, y = check_list.popleft()
    if x == n-1 and y == m-1:
        break

    for i in range(4):
        temp_x = x
        temp_y = y
        temp_x += dx[i]
        temp_y += dy[i]
        
        if temp_x < 0 or temp_y < 0 or temp_x >= n or temp_y >= m:
            continue
        if arr[temp_x][temp_y] == 0:
            continue
        if arr[temp_x][temp_y] == 1:
            arr[temp_x][temp_y] = arr[x][y] + 1
            check_list.append([temp_x,temp_y])

print(arr[n-1][m-1])

  
