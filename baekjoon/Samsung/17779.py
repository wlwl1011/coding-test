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

answer = 1e9
for x in range(1,n+1):
    for y in range(1,n+1):
        
        # print("criteria:",x,y)
        sum = [0 for _ in range(5)]
        #기준점에 따른 경계의 길이를 정한다.
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):    
                #가능한 길이의 조합을 담아놓는다.
                
                if x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <=n:
                    sum = [0 for _ in range(5)]
                    check_arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
                    #print("length:",d1,d2)
                    #경계를 나눈다
                    for i in range(d1+1):
                        check_arr[x+i][y-i] = 5 
                        check_arr[x+d2+i][y+d2-i] = 5
                    for j in range(d2+1):
                        check_arr[x+j][y+j] = 5
                        check_arr[x+d1+j][y-d1+j] = 5
                    #print("print criteria")
                    # for i in range(n+1):
                    #     print(check_arr[i])        
                    #그 속도 채운다....
                    for i in range(x+1, x+d1+d2):
                        flag = False
                        for j in range(1,n+1):
                            if check_arr[i][j] == 5:
                                flag = not flag
                            if flag:
                                check_arr[i][j] = 5
                    # print("~inner~")
                    # for i in range(n+1):
                    #     print(check_arr[i])               
                    for r in range(1,n+1):
                        for c in range(1,n+1):
                            if check_arr[r][c] == 5:
                                continue
                            if 1 <= r < x + d1 and 1 <= c <= y:
                                check_arr[r][c] = 1
                            elif  1 <= r <= x + d2 and y < c <= n:   
                                check_arr[r][c] = 2  
                            elif x + d1  <= r <= n and 1 <= c < y - d1 + d2 :
                                check_arr[r][c] = 3
                            elif x + d2 < r <= n and y - d1 + d2 <= c <= n:
                                check_arr[r][c] = 4
                            else:
                                check_arr[r][c] = 5
                    # print("print arr")
                    # for i in range(n+1):
                    #     print(arr[i])
                    # print("check_arr")    
                    # for i in range(n+1):
                    #     print(check_arr[i])

                    for r in range(1,n+1):
                        for c in range(1,n+1):   
                            sum[check_arr[r][c]-1] += arr[r][c]                 
                    # print("sum : ",sum , "diff : ", max(sum) - min(sum))
                    answer = min( answer, max(sum) - min(sum) )       

                
print(answer)


            
                
