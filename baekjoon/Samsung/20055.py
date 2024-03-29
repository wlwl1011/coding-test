import sys, os, io, atexit
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

N, K = map(int, input().split())
A = list(map(int, input().split()))
arr = [0] * ( 2 * N ) 
count = 0
size = (2 * N) - 1
number = 1
robot = {}

while True:
    count += 1
    #슬라이싱을 통한 복사가 copy 보다 빠르다
    arr_copy = arr[:]
    A_copy = A[:]
    
    for i in range(0, 2*N):

        #벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
        #벨트가 한 칸 회전하면 1번부터 2N-1번까지의 칸은 다음 번호의 칸이 있는 위치로 이동하고, 
        #2N번 칸은 1번 칸의 위치로 이동한다. i번 칸의 내구도는 Ai
        A[i] = A_copy[i-1] 
        arr[i] = arr_copy[i-1]
    
    if arr[N-1] != 0: #만약 내리는 위치에 로봇이 있으면 내리자
        # print(arr)
        # print(robot)
        del robot[arr[N-1]]
        arr[N-1] = 0   
    robot_size = len(robot)

    temp = []
    for num in robot:
    
        #가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
        #로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
        
        arr_copy = arr[:]
 
        for i in range(size+1):
            
            if num == arr[i] : #그 순서에 해당되고 
                if  arr[(i+1)% size] == 0  and A[i+1] > 0: # 이동하려는 칸에 로봇이 없고 내구도의 값이 있다면
                    arr[(i+1)% size] = arr_copy[i]
                    arr[i] = 0
                    A[i+1] -= 1
                break    
       

        #내리는 위치에 로봇이 있으면
        if arr[N-1] != 0: #만약 내리는 위치에 로봇이 있으면 내리자
            temp.append(arr[N-1])
            
            arr[N-1] = 0            
    for i in temp:
        del robot[i]            
    #올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.  
    if A[0] > 0 and arr[0] == 0: 
        arr[0] = number
        robot[number] = 0
        number +=1
        A[0] -=1
    if arr[N-1] != 0: #만약 내리는 위치에 로봇이 있으면 내리자
        # print(arr)
        # print(robot)
        del robot[arr[N-1]]
        arr[N-1] = 0   

    temp = 0
    for i in A:
        if i == 0:   
            temp += 1

    
    #print(temp)        
    if temp >= K:
        break      


print(count)    
