import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

w,h = map(int,input().split())
n = int(input())

arr = []

for _ in range(n):
    temp = list(map(int,input().split()))
    arr.append(temp)

d, l = map(int,input().split())

answer = 0

for i in arr:
    direction, length = i[0], i[1]

    if d ==1 or d ==2 : #북 혹은 남
        if direction == 1 or direction == 2: #북 혹은 남
            if d == direction:
                answer += abs(length-l)
            else:
                if length + l < w-length + w-l:
                    answer += length + l + h
                else:
                    answer += w-length + w-l+ h       

        elif direction ==3: #서쪽
            if d == 1: 
                answer += l + length
            else:
                answer += l + h - length    

        elif direction == 4: #동쪽
            if d == 1:
                answer += w-l + length  
            else:
                answer += w-l + h - length      

       
    else: #동 혹은 서 
        if direction == 3 or direction == 4: #동 혹은 서
            if d == direction:
                answer += abs(length-l)
            else:
                if length + l < h-length + h-l:
                    answer += length + l + w
                else:
                    answer += h-length + h-l+ w     
        elif direction ==1: #북쪽
            if d == 3: #서쪽
                answer += l + length
            else:
                answer += l + h - length    

        elif direction == 4: #남쪽
            if d == 1:
                answer += w-l + length  
            else:
                answer += w-l + h - length                
                    
print(answer)                    
        


