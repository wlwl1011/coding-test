import sys, os, io, atexit
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s:stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

global answer

def check(i,j,value):
    global answer

    if 0<= i < N and 0 <= j < N:
        arr[i][j] += value
    else: 
        answer += value
           

def solve(arr):
    
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1 ,0] 

    r = N//2
    c = N//2

    while True:
     #copy_arr = arr[:]
        if r == 0 and c == 0:
            print(answer)
            break
        for i in range(4):
            tr = r + dx[i]
            tc = c + dy[i]
            if 0 <= tr < N and 0<= tc < N:
            #모레의 양
                y = arr[tr][tc] 

                if i == 1:
                    #1%
                    check(r-1,c,int( y * 0.01))
                    check(r+1,c,int( y * 0.01)) 
                    #7%
                    check(tr-1,tc,int( y * 0.07)) 
                    check(tr+1,tc,int( y * 0.07))
                    #2%
                    check(tr-2,tc,int( y * 0.02))
                    check(tr+2,tc,int( y * 0.02))       
                    #10%   
                    check(tr-1,tc-1,int( y * 0.1))
                    check(tr+1,tc-1,int( y * 0.1))  
                    #5%
                    check(tr,tc-2,int( y * 0.05))
                    #a 
                    check(tr,tc-1,int(y))         

                elif i == 2:
                    #1%
                    check(r, c-1, int( y  * 0.01))
                    check(r, c+1, int( y  * 0.01))
                    #7%
                    check(tr, tc-1, int( y * 0.07))
                    check(tr, tc+1, int( y * 0.07))
                    #2%
                    check(tr, tc-2, int( y * 0.02))
                    check(tr, tc+2, int( y * 0.02))
                    #10%
                    check(tr-1, tc+1, int( y * 0.1))
                    check(tr+1, tc+1, int( y * 0.1))
                    #5%
                    check(tr-2, tc, int( y * 0.05 ))
                    #a
                    check(tr-1,tc, int(y))

                elif i == 3:

                elif i == 4:           
            #dx dy 값 갱신 해줘야함        

answer = 0
N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

