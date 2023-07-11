import sys, os, io, atexit
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))
import copy

def fish_move(fish, direction, shark_index, shark_direction,answer):

    # print("Before ---- ",answer)
    # print("fish")
    # for i in range(4):
    #     for j in range(4):
    #         print(fish[i][j],end=' ')
    #     print()    
    # print("direction")
    # for i in range(4):
    #     for j in range(4):
    #         print(direction[i][j],end=' ')
    #     print()      

    for number in range(1,17):
        flag = False
        for x in range(4):
            if flag == True:
                break
            for y in range(4):
                #물고기는 번호가 작은 물고기부터 순서대로 이동
                fish_data = fish[x][y]
                direction_data = direction[x][y]
                
                if fish_data == number:
                    flag = True
                    
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
                    # print("when",number)    
                    # print("fish")
                    # for i in range(4):
                    #     for j in range(4):
                    #         print(fish[i][j],end=' ')
                    #     print()    
                    # print("direction")
                    # for i in range(4):
                    #     for j in range(4):
                    #         print(direction[i][j],end=' ')
                    #     print()   
                       
                          
                    break   
                else:
                    continue  

    # print("After ---- ")
    # print("fish")
    # for i in range(4):
    #     for j in range(4):
    #         print(fish[i][j],end=' ')
    #     print()    
    # print("direction")
    # for i in range(4):
    #     for j in range(4):
    #         print(direction[i][j],end=' ')
    #     print()    


    # print("Shark eating ..." , shark_index, shark_direction)                  
    #전달받은 상어 위치에서 ~ 상어가 이제 어디갈지 정해보쟈미
    sx = shark_index[0] + dx[shark_direction-1]
    sy = shark_index[1] + dy[shark_direction-1]

    #근데 새로 갈 방향이 경계를 벗어나면?
    #그냥 끝이지
    fish_list = []

    if sx < 0 or sx >=4 or sy < 0 or sy >= 4:
        # print("out!!!!!!!!!!!!!!!")
        return answer
    if fish[sx][sy] != -1:
        fish_list.append([sx,sy])
    #경계 안 벗어남
    #그냥 가능한 물고기들을 다 해서 Index로 넘겨줘야함 ? 그런듯
    

    while True: #범위 안에서 물고기가 있는 칸으로 ..
        sx += dx[shark_direction-1]
        sy += dy[shark_direction-1]
        #범위를 벗어나면 안됨!
        if sx < 0 or sx >=4 or sy < 0 or sy >= 4:
            break
        if fish[sx][sy] == -1:
            continue
        #범위를 벗어나지 않고 물고기가 있는 칸을 찾았니?
        else:
            #그러면 걔네가 상어가 먹는 것이 다 가능한 애들이야.. 최고의 결과 값을 찾아야해
            fish_list.append([sx,sy])
            #그러면 나가자
    # print(fish_list)        
    temp = answer
    for i, j in fish_list:
        # print(i,j)
        temp_answer = temp
        temp_answer += fish[i][j]
        shark_index = [i, j]
        shark_direction =  direction[i][j]
        # print(shark_index,shark_direction)
        fish_copy = copy.deepcopy(fish)
        direction_copy = copy.deepcopy(direction)
        fish_copy[i][j] = -1
        direction_copy[i][j] = -1   
        # print("Shark eating finish ....," , shark_index, shark_direction,temp_answer)      
        # print("fish")
        # for i in range(4):
        #     for j in range(4):
        #         print(fish[i][j],end=' ')
        #     print()    
        # print("direction")
        # for i in range(4):
        #     for j in range(4):
        #         print(direction[i][j],end=' ')
        #     print()    
        
        # print("max?",temp)
        answer = max(answer , fish_move(fish_copy, direction_copy, shark_index, shark_direction,temp_answer)) 
        
        #최고 값이라면 ~
    return answer


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

answer = 0
shark_index = [0,0]
shark_direction = direction[0][0]
#빈칸은 -1로 표현한다.
answer += fish[0][0]
fish[0][0] = -1
direction[0][0] = -1

print(fish_move(fish, direction, shark_index, shark_direction, answer))


