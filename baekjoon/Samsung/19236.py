import sys, os, io, atexit
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

#번호, 방향
# 1<= 번호 <= 16 / 겹치지 않음
# 방향은 8가지 상하좌우, 대각선

dx = [-1, -1, 0, 1, 1, 1, 0,-1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

fish = [ [ 0 for _ in range(4) ] for _ in range(4) ]
direction = [ [ 0 for _ in range(4) ] for _ in range(4) ]

for i in range(4):
    temp = list(map(int, input().split()))
    fish[i] = temp[0::2]
    direction[i] = temp[1::2]

####
####
####
####

#청소년 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어가게 된다. 
# 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다. 이후 물고기가 이동한다.

#i, j, direction
answer = 0
shark_index = [0,0]
shark_direction = direction[0][0]
#빈칸은 -1로 표현한다.
answer += fish[0][0]
fish[0][0] = -1
direction[0][0] = -1


def fish_move(fish, direction):
     for number in range(1,16+1):
        for x in range(4):
            for y in range(4):
                #물고기는 번호가 작은 물고기부터 순서대로 이동
                fish_data = fish[x][y]
                direction_data = direction[x][y]
                #1번부터 차례대로 상어를 먹는다 냠냠
                if fish_data == number:
                    #direction_data 은 1부터 8까지의 값이다.
                    nx = x + dx[direction_data-1]
                    ny = y + dy[direction_data-1]
                    
                    #상어가 있거나, 공간의 경계를 넘어가 이동할 수 없다면,
                    # 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 45도 반시계 회전
                    
                    if [nx,ny] == shark_index or nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                        new_direction = direction_data-1
                        for i in range(1,8):
                            new_direction += 1
                            if new_direction > 7:
                                new_direction = 0
                            cx = x + dx[new_direction]
                            cy = y + dy[new_direction]
                            #상어도 없고
                            #공간의 경계안에 있다면 ! 그 방향이닷 !!!!
                            if [cx,cy] != shark_index and 0 <= cx < 4 and 0 <= cy < 4:
                                nx = cx
                                ny = cy
                                #그럼 방향도 업데이터 해줘야지.
                                direction[x][y] = new_direction + 1
                                #
                                fish_temp = fish[nx][ny]
                                fish[nx][ny] = fish[x][y]
                                fish[x][y] = fish_temp
                                #
                                direction_temp = direction[nx][ny]
                                direction[nx][ny] = direction[x][y]
                                direction[x][y] = direction_temp
                                break
                    #애초에 갈 수 있었으면 그냥 하면 된다.
                    else:                 
                        #
                        fish_temp = fish[nx][ny]
                        fish[nx][ny] = fish[x][y]
                        fish[x][y] = fish_temp
                        #
                        direction_temp = direction[nx][ny]
                        direction[nx][ny] = direction[x][y]
                        direction[x][y] = direction_temp
                    break   
        shark_eat()        

def shark_eat():
    sx = shark_index[0] + dx[shark_direction-1]
    sy = shark_index[1] + dy[shark_direction-1]
    #근데 새로 갈 방향이 경계를 벗어나면?
    if sx < 0 or sx >=4 or sy < 0 or sy >= 4:
        return

    #경계 안 벗어남
    flag = True
    if fish[sx][sy] == -1: #물고기가 없다
        #싹다 디빈다.
        while True: #범위 안에서 물고기가 있는 칸으로 ..
            sx += dx[shark_direction-1]
            sy += dy[shark_direction-1]
            #범위를 벗어나면 안됨!
            if sx < 0 or sx >=4 or sy < 0 or sy >= 4:
                flag = False
                break
            #범위를 벗어나지 않고 물고기가 있는 칸을 찾았니?
            if fish[sx][sy] != -1:
                #그러면 나가자
                break

        if flag: #그 범위를 찾은겨
            shark_index = [sx, sy]
            shark_direction = direction[sx][sy]
            answer += fish[sx][sy]
            fish[sx][sy] = -1
            direction[sx][sy] = -1    
        else:
            return        
    #그냥 바로 물고기가 있을 수도 있자나
    else:
        shark_index = [sx, sy]
        shark_direction = direction[sx][sy]
        answer += fish[sx][sy]
        fish[sx][sy] = -1
        direction[sx][sy] = -1      


while True: 
    #물고기의 이동      
    fish_move()
   
               
print(answer)


