import sys, os, io, atexit
from collections import deque
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m = map(int,input().split())
arr = []
for _ in range(n):
    temp = list(map(int,input().split()))
    arr.append(temp)

dx = [-1, 1, 0, 0]  
dy = [0, 0, -1, 1]

answer = 0
check_list = deque()
check_list.append([0,0])
while check_list:
    print(check_list)
    x, y = check_list.pop()
    if x == n-1 and y == m-1:
        break
    answer +=1
    for i in range(4):
        temp_x = x
        temp_y = y
        temp_x += dx[i]
        temp_y += dy[i]
        
        if temp_x < 0 or temp_y < 0 or temp_x > n-1 or temp_y > m-1:
            continue
        print(temp_x,temp_y)
        if arr[temp_x][temp_y] == 1:
            check_list.append([temp_x,temp_y])

print(answer)

  
