import sys, os, io, atexit
from collections import deque
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int,input())))

dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]
check = 1

queue = deque()
check_list = []
sum = [0 for i in range(n*n)]
for k in range(0,n):
    for t in range(0,n):
        #print(k,t)
        if arr[k][t] != 1:
            continue
        queue.append([k,t])
        check += 1 
        #print(queue)
        #print(check)   
        while queue:
            x, y = queue.popleft()
            for i in range(5):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >=n or ny >=n :
                    continue
                if arr[nx][ny] == 0:
                    continue
                if arr[nx][ny] == 1:
                    arr[nx][ny] = check
                    sum[check] +=1
                    queue.append([nx,ny])
                    
# for i in range(n):
#     print(arr[i])
print(check-1) 
sum.sort()
for i in sum:
    if i !=0:
        print(i)
