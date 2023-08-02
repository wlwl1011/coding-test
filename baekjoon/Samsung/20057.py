import sys
input = sys.stdin.readline

# 방향 왼쪽, 아래, 오른쪽, 위
dx = [0,1,0,-1]
dy = [-1,0,1,0]

# 각 방향에 따른 비율
left = [[0,0,2,0,0],[0,10,7,1,0],[5,'a',0,0,0],[0,10,7,1,0],[0,0,2,0,0]]
down = [[0,0,0,0,0],[0,1,0,1,0], [2,7,0,7,2], [0,10,'a',10,0], [0,0,5,0,0]]
right = [[0,0,2,0,0],[0,1,7,10,0],[0,0,0,'a',5],[0,1,7,10,0],[0,0,2,0,0]]
up = [[0,0,5,0,0],[0,10,'a',10,0],[2,7,0,7,2],[0,1,0,1,0],[0,0,0,0,0]]


# d방향으로 cnt 만큼 반복하며 이동
def move(cnt, d, rate):
    global answer
    global x,y
    global array

    for _ in range(cnt+1):
        # 이동한 위치
        x += dx[d]
        y += dy[d]
        a_loca = [] # a의 좌표값 저장
        temp = 0  # 흩어진 모래의 총값
        # x,y좌표를 rate 배열 좌표 중앙에 존재하도록 이동
        a, b = x-2, y-2


        # 토네이도는 (1, 1)까지 이동한 뒤 소멸한다
        # -> 1행1열에서 소멸한다 -> 좌표값은 (0,0)임
        # (0, 0) 지점에 도달하는 경우 종료
        if x < 0 or y <0:
            # print("break")
            break

        # 모래 흩어지기
        for i in range(5):
            for j in range(5):
                if rate[i][j] !=0 and rate[i][j] !='a':
                    if -1< a+i <n and -1< b+j <n: # 격자 안에 존재할 경우
                        array[a+i][b+j] += array[x][y]*rate[i][j]//100
                    else: # 격자 밖으로 나갈 경우
                        answer += array[x][y]*rate[i][j]//100
                    # a값 구하기 위해 흠어진 모래양 temp에 더해주기
                    temp += array[x][y]*rate[i][j]//100
                elif rate[i][j] =='a': # a 좌표 기억
                    a_loca = [i,j]

        # 흩어지고 남은 모래 처리하기
        a_x,a_y = a_loca
        if -1< a+a_x < n and -1< b+a_y < n: # 격자 안에 존재할 경우 좌표에 더해줌
            array[a+a_x][b+a_y] += array[x][y] -temp
        else: # 격자 밖으로 나갈 경우 answer에 더해줌
            answer+=array[x][y] -temp
        array[x][y] = 0

n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

x,y = n//2, n//2 # 처음 시작 좌표
answer = 0 # 격자 밖으로 나간 모래양

# 달팽이 모양으로 돌기
for i in range(n):
    if i%2 == 0:
        move(i, 0, left)
        move(i, 1, down)
    else:
        move(i, 2, right)
        move(i, 3, up)

print(answer)