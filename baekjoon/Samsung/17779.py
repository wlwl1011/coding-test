import sys, os, io, atexit
import copy
from collections import deque
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())

arr = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n):
    temp = list(map(int, input().split()))
    arr[i+1][1:] = temp



answer = 1000
for i in range(1,n+1):
    for j in range(1,n+1):
        # print('[',i,j,']')  
        check_arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
        sum = [0 for _ in range(n+1)]
        length = []
        #기준점에 따른 경계의 길이를 정한다.
        for d1 in range(1, j):
            for d2 in range(1, n - j + 1):
                if d1 + d2 <= n - i:
                    length.append([d1, d2])
                    #가능한 길이의 조합을 담아놓는다.
        if len(length) == 0:
            continue
        # print("length : ",length)     

        for d1, d2 in length:       
            #경계선
            for r in range(d1+1):
                for c in range(d2+1):
                    check_arr[i+r][j-r] = 5 
                    check_arr[i+c][j+c] = 5
                    check_arr[i+d1+c][j-d1+c] = 5
                    check_arr[i+d2+r][j+d2-r] = 5
            # print("criteria")            
            # for inedx in range(n+1):
            #     print(check_arr[inedx]) 
            for r in range(1,n+1):
                for c in range(1,n+1):
                    if check_arr[r][c] == 5:
                        continue
                    if r < i + d1 and c <= j:
                        check_arr[r][c] = 1   
                    elif  r <= i + d2 and j < c <= n:   
                        check_arr[r][c] = 2  
                    elif i + d1  <= r <= n and 1<= c < j - d1 + d2 :
                        check_arr[r][c] = 3
                    elif i + d2 < r <= n and j - d1 + d2 <= c <= n:
                        check_arr[r][c] = 4
                    else:
                        check_arr[r][c] = 5
            # print("d1,d2 :" ,d1,d2)            
            # for inedx in range(n+1):
            #     print(check_arr[inedx])     
                 
            for r in range(1,n+1):
                for c in range(1,n+1):   
                    sum[check_arr[r][c]] += arr[r][c]                 
            temp_min = 1000
            temp_max = 0
            for index in range(1,n+1):
                if sum[index] == 0:
                    continue
                if sum[index] > temp_max:
                    temp_max = sum[index]
                if sum[index] < temp_min:
                    temp_min = sum[index]    
            answer = min( answer, temp_max -temp_min )       

                
print(answer)


            
                
