import sys, os, io, atexit
import copy
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

arr = [[] for _ in range(4)]

for i in range(4):
    arr[i] = list(map(int, input()))

k = int(input())

for i in range(k):
    num, rotate = map(int, input().split())
    temp_arr = copy.deepcopy(arr[num-1])
    check_arr = copy.deepcopy(arr)

    #반시계 방향
    if rotate == -1:
        for i in range(8):
            if i == 7:
                arr[num-1][7] = temp_arr[0]
            else:    
                arr[num-1][i] = temp_arr[i+1]
    #시계 방향            
    else:
        for i in range(8):
           if i == 0:
                arr[num-1][0] = temp_arr[7]
           else:    
                arr[num-1][i] = temp_arr[i-1]

    #지금 돌린 애 옆에 있어서 저절로 돌아가는 애들 ..
    
    if num-1 == 0 :
        
        if check_arr[0][2] != check_arr[1][6]:
            #극이 다르면 돌려야지    

            #근데 그걸 반대로
            rotate = -(rotate)
            temp_arr = copy.deepcopy(arr[1]) #2번 배열 복사
            #반시계 방향
            if rotate == -1:
                for i in range(8):
                    if i == 7:
                        arr[1][7] = temp_arr[0]
                    else:    
                        arr[1][i] = temp_arr[i+1]
            #시계 방향            
            else:
                for i in range(8):
                    if i == 0:
                        arr[1][0] = temp_arr[7]
                    else:    
                        arr[1][i] = temp_arr[i-1]

            #2번이 돌아갔으니까 3번도 돌려야지         
            if check_arr[1][2] != check_arr[2][6]: 

                #근데 그걸 반대로
                rotate = -(rotate)
                temp_arr = copy.deepcopy(arr[2]) #3번 배열 복사
                #반시계 방향
                if rotate == -1:
                    for i in range(8):
                        if i == 7:
                            arr[2][7] = temp_arr[0]
                        else:    
                            arr[2][i] = temp_arr[i+1]
                #시계 방향            
                else:
                    for i in range(8):
                        if i == 0:
                            arr[2][0] = temp_arr[7]
                        else:    
                            arr[2][i] = temp_arr[i-1]

                #3번이 돌아갔으니까 4번이 돌아가야지
                if check_arr[2][6] != check_arr[3][2]: 

                    #근데 그걸 반대로
                    rotate = -(rotate)
                    temp_arr = copy.deepcopy(arr[3]) #4번 배열 복사
                    #반시계 방향
                    if rotate == -1:
                        for i in range(8):
                            if i == 7:
                                arr[3][7] = temp_arr[0]
                            else:    
                                arr[3][i] = temp_arr[i+1]
                    #시계 방향            
                    else:
                        for i in range(8):
                            if i == 0:
                                arr[3][0] = temp_arr[7]
                            else:    
                                arr[3][i] = temp_arr[i-1]    
                            
    elif num-1 == 1 :
        temp_rotate_1 = rotate
        temp_rotate_2 = rotate
        if check_arr[0][2] != check_arr[1][6]:
            #극이 다르면 돌려야지    

            #근데 그걸 반대로
            temp_rotate_1 = -(temp_rotate_1)
            temp_arr = copy.deepcopy(arr[0]) #0번 배열 복사
            #반시계 방향
            if temp_rotate_1 == -1:
                for i in range(8):
                    if i == 7:
                        arr[0][7] = temp_arr[0]
                    else:    
                        arr[0][i] = temp_arr[i+1]
            #시계 방향            
            else:
                for i in range(8):
                    if i == 0:
                        arr[0][0] = temp_arr[7]
                    else:    
                        arr[0][i] = temp_arr[i-1]
        # 3번도 돌려야지         
        if check_arr[1][2] != check_arr[2][6]: 

            #근데 그걸 반대로
            temp_rotate_2 = -(temp_rotate_2)
            temp_arr = copy.deepcopy(arr[2]) #3번 배열 복사
            #반시계 방향
            if temp_rotate_2 == -1:
                for i in range(8):
                    if i == 7:
                            arr[2][7] = temp_arr[0]
                    else:    
                            arr[2][i] = temp_arr[i+1]
                #시계 방향            
                else:
                    for i in range(8):
                        if i == 0:
                            arr[2][0] = temp_arr[7]
                        else:    
                            arr[2][i] = temp_arr[i-1]

                #3번이 돌아갔으니까 4번이 돌아가야지
                if check_arr[2][2] != check_arr[3][6]: 

                    #근데 그걸 반대로
                    temp_rotate_2 = -(temp_rotate_2)
                    temp_arr = copy.deepcopy(arr[3]) #4번 배열 복사
                    #반시계 방향
                    if temp_rotate_2 == -1:
                        for i in range(8):
                            if i == 7:
                                arr[3][7] = temp_arr[0]
                            else:    
                                arr[3][i] = temp_arr[i+1]
                    #시계 방향            
                    else:
                        for i in range(8):
                            if i == 0:
                                arr[3][0] = temp_arr[7]
                            else:    
                                arr[3][i] = temp_arr[i-1]    

    elif num-1 == 2 :
        temp_rotate_1 = rotate
        temp_rotate_2 = rotate
        #2번이랑 3번이랑 다르면 2번을 돌리자
        if check_arr[1][2] != check_arr[2][6]: 

            #근데 그걸 반대로
            temp_rotate_1 = -(temp_rotate_1)
            temp_arr = copy.deepcopy(arr[1]) #2번 배열 복사
            #반시계 방향
            if temp_rotate_2 == -1:
                for i in range(8):
                    if i == 7:
                            arr[1][7] = temp_arr[0]
                    else:    
                            arr[1][i] = temp_arr[i+1]
                #시계 방향            
                else:
                    for i in range(8):
                        if i == 0:
                            arr[1][0] = temp_arr[7]
                        else:    
                            arr[1][i] = temp_arr[i-1]
            #2번이랑 1번이랑 다르면 1번을 돌리자
            if check_arr[0][2] != check_arr[1][6]:
            #극이 다르면 돌려야지    

                #근데 그걸 반대로
                temp_rotate_1 = -(temp_rotate_1)
                temp_arr = copy.deepcopy(arr[0]) #0번 배열 복사
                #반시계 방향
                if temp_rotate_1 == -1:
                    for i in range(8):
                        if i == 7:
                            arr[0][7] = temp_arr[0]
                        else:    
                            arr[0][i] = temp_arr[i+1]
                #시계 방향            
                else:
                    for i in range(8):
                        if i == 0:
                            arr[0][0] = temp_arr[7]
                        else:    
                            arr[0][i] = temp_arr[i-1]      
         #3번이 돌아갔으니까 4번이 돌아가야지
        if check_arr[2][2] != check_arr[3][6]: 

            #근데 그걸 반대로
            temp_rotate_2 = -(temp_rotate_2)
            temp_arr = copy.deepcopy(arr[3]) #4번 배열 복사
            #반시계 방향
            if temp_rotate_2 == -1:
                for i in range(8):
                    if i == 7:
                        arr[3][7] = temp_arr[0]
                    else:    
                        arr[3][i] = temp_arr[i+1]
            #시계 방향            
            else:
                for i in range(8):
                    if i == 0:
                        arr[3][0] = temp_arr[7]
                    else:    
                        arr[3][i] = temp_arr[i-1]     
    else :
        #4번이랑 3번 비교
        if check_arr[2][2] != check_arr[3][6]: 

            #근데 그걸 반대로
            rotate = -(rotate)
            temp_arr = copy.deepcopy(arr[2]) #3번 배열 복사
            #반시계 방향
            if rotate == -1:
                for i in range(8):
                    if i == 7:
                        arr[2][7] = temp_arr[0]
                    else:    
                        arr[2][i] = temp_arr[i+1]
            #시계 방향            
            else:
                for i in range(8):
                    if i == 0:
                        arr[2][0] = temp_arr[7]
                    else:    
                        arr[2][i] = temp_arr[i-1]    

            #3번이랑 2번 비교
            if check_arr[1][2] != check_arr[2][6]: 

                #근데 그걸 반대로
                rotate = -(rotate)
                temp_arr = copy.deepcopy(arr[1]) #2번 배열 복사
                #반시계 방향
                if rotate == -1:
                    for i in range(8):
                        if i == 7:
                            arr[1][7] = temp_arr[0]
                        else:    
                            arr[1][i] = temp_arr[i+1]
                #시계 방향            
                else:
                    for i in range(8):
                        if i == 0:
                            arr[1][0] = temp_arr[7]
                        else:    
                            arr[1][i] = temp_arr[i-1]
                #2번이랑 1번 비교
                if check_arr[0][2] != check_arr[1][6]:
                    #극이 다르면 돌려야지    

                    #근데 그걸 반대로
                    rotate = -(rotate)
                    temp_arr = copy.deepcopy(arr[0]) #2번 배열 복사
                    #반시계 방향
                    if rotate == -1:
                        for i in range(8):
                            if i == 7:
                                arr[0][7] = temp_arr[0]
                            else:    
                                arr[0][i] = temp_arr[i+1]
                    #시계 방향            
                    else:
                        for i in range(8):
                            if i == 0:
                                arr[0][0] = temp_arr[7]
                            else:    
                                arr[0][i] = temp_arr[i-1]

sum = 0
if arr[0][0] == 1:
    sum += 1
if arr[1][0] == 1:
    sum += 2
if arr[2][0] == 1:
    sum += 4
if arr[3][0] == 1:
    sum += 8

print(sum)

   