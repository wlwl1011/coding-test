import sys, os, io, atexit
import copy
from collections import deque
import heapq
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

queue = deque()
#청소년 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어가게 된다. 
# 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다. 이후 물고기가 이동한다.

#i, j, direction
shark_index = [0,0]
shark_direction = direction[0][0]
fish[0][0] = 1e9
direction[0][0] = 1e9

while True: 
    copy_fish = copy.deepcopy(fish)
    copy_direction = copy.deepcopy(direction)
    for number in range(16):
        for x in range(4):
            for y in range(4):
                #물고기는 번호가 작은 물고기부터 순서대로 이동
                fish_data = copy_fish[x][y]
                direction_data = copy_direction[x][y]
                if copy_fish[x][y] == number:
                    #direction_data 은 1부터 8까지의 값이다.
                    nx = x + dx[direction_data-1]
                    ny = y + dy[direction_data-1]
                    # 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 45도 반시계 회전
                    if [nx,ny] == shark_index or nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                        for i in range(1,8):
                            new_direction = direction_data-1-i
                            if new_direction < 0:
                                new_direction = 8
                            nx = x + dx[new_direction]
                            ny = y + dy[new_direction]
                            if [nx,ny] != shark_index and 0 <= nx < 4 and 0 <= ny < 4:
                                break
                    fish[nx][ny] = copy_fish[x][y]
                    fish[x][y] = copy_fish[nx][ny]
                    direction[nx][ny] = copy_direction[x][y]
                    direction[x][y] = copy_direction[nx][ny]

                      

#상어의 방향은 물고기의 방향과 같아짐. 이후 물고기가 이동함
    
#물고기는 번호가 작은 물고기부터 순서대로 이동
#한칸 이동, 이동 할 수 있는 칸은 빈칸과 다른 물고리가 있는 칸
#이동할 수 없는 칸은 상어가 있거나 공간의 경계를 넘는 경우
# 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 45도 반시계 회전
# 만약 없으면 안 함
    i, j = queue.popleft()
    shark_direction = fish[i][j]   
    fish[i][j] = 1e9
    direction[i][j] = 1e9

#물고기의 이동이 끝나면 상어가 이동함
#상어는 방향에 있는 칸으로 이동할 수 있음
#물고기가 있는 칸으로 이동할 경우 그 칸의 물고리를 먹음
#그 물고기의 방향을 가짐
#꼭 물고기가 있는 칸으로 이동함
#상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로감

