import sys, os, io, atexit
import copy
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, l = map(int, input().split())

arr = [ [0 for _ in range(n)] for _ in range(n) ]

for i in range(n):
    arr[i] = list(map(int, input().split()))

temp_arr = copy.deepcopy(arr)

answer = 0
for i in range(n):
    #가로부터 출발하자
    count = 0
    flag = False
    for j in range(n):
        if j-1 < 0 : #범위 밖의 값이면 넘어가라
            count = 1
            continue
        if abs(temp_arr[i][j-1] - arr[i][j]) >= 2 : #높이는 1차이 나야한다
            break
        if temp_arr[i][j-1] - arr[i][j] == 1: 
            if flag and count < l:
                break
            count = 1
            flag = True
        if temp_arr[i][j-1] - arr[i][j] == -1:
            
            if flag and count < l:
                break
            elif flag  and count > l:
                flag = False
                count = count - l
            elif flag and count == l:
                break
          
            if count :
                if count >= l:
                    count = 1
                else:
                    break
            else:
                count = 1       
        if temp_arr[i][j-1] - arr[i][j] == 0 : 
            #높이가 같은 경우는 사다리를 설치할 수 있는 길이가 되는지 확인해야한다.
            count = count + 1 
    

            #우리는 필요한 만큼만 있으면 된다.
        if j == n-1:
            if flag and count < l:
                break
            answer += 1  
            # print(i,j)  

for i in range(n):
    #세로 출발하자
    count = 0
    flag = False
    for j in range(n):
        if j-1 < 0 : #범위 밖의 값이면 넘어가라
            count = 1
            continue
        if abs(temp_arr[j-1][i] - arr[j][i]) >= 2 : #높이는 1차이 나야한다
            break
        if temp_arr[j-1][i] - arr[j][i] == 1:
            if flag and count < l:
                break
            count = 1
            flag = True
        if temp_arr[j-1][i] - arr[j][i] == -1:   
            if flag and count < l:
                break
            elif flag  and count > l:
                flag = False
                count = count - l
            elif flag and count == l:
                break    
            if count :
                if count >= l:
                    count = 1
                else:
                    break
            else:
                count = 1      
        if temp_arr[j-1][i] - arr[j][i] == 0 : 
            #높이가 같은 경우는 사다리를 설치할 수 있는 길이가 되는지 확인해야한다.
            count = count + 1 
           
        if j == n-1:
            if flag and count < l:
                break
            answer += 1  
            # print(j,i) 
           
        
print(answer)

