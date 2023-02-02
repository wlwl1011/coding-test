import sys

a,b,c,m = map(int, sys.stdin.readline().split())

#a : 피로도 쌓이는 정도
#b : 일을 처리 할 수 있는 정도
#c : 피로도가 줄어드는 정도
#m : 피로도 최대량

check = 0
work = 0



for i in range(24):


    #만약 피로도가 최대치를 넘지 않으면
    if check + a <= m :
        work = work + b # 일의 양 누적
        check = check + a # 피로도 누적
       

    else :
         #쉬어라
        check = check - c

        if check < 0:
            check = 0

    
print(work)       

        

    