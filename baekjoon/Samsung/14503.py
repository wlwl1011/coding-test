import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())

r, c, d = map(int, input().split())

arr = [[1 for _ in range(m)] for _ in range(n)]



for i in range(n):
    temp = list(map(int, input().split()))
    arr[i] = temp

x = r
y = c

count = 1
arr[x][y] = 1
while True:
    #범위를 초과하지 않아야함
    if x >= 0 and y >= 0 and x < n and y < m :
        #현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우가 있는지 확인
        flag = True
        for _ in range(4):
            d = (d+3)%4
            cx = x + dx[d]
            cy = y + dy[d]
            if cx >= 0 and cy >= 0 and cx < n and cy < m:
                if arr[cx][cy] == 0:
                    flag = False
                    x = cx
                    y = cy
                    arr[cx][cy] = 1
                    count +=1
                    #현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
                    #반시계 방향으로 90 회전한다.
                    break
                    
        #현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우            
        if flag == True:
            cx = x - dx[d]
            cy = y - dy[d]
                    
            #한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            if cx >= 0 and cy >= 0 and cx < n and cy < m:
                if arr[cx][cy] == 1:
                    #바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
                    break    
                else:
                    #바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진
                    x = cx
                    y = cy
                    
            
             
print(count)