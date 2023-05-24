import sys, os, io, atexit
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

photo_frame = int(input())

n = int(input())

arr = list(map(int,input().split()))

photo_num = {}
frame_check = []

for i in range(1,n+1):
    photo_num[i] = 0

for i in arr:
    #print(len(frame_check) ,photo_frame)
    #print(frame_check)   
    if [i, photo_num[i]] in frame_check:
        #frame_check.pop(frame_check.index([i, photo_num[i]]))
        photo_num[i] += 1
        frame_check[frame_check.index([i, photo_num[i]-1])] = [i, photo_num[i]]
    elif len(frame_check) < photo_frame:
        photo_num[i] += 1
        frame_check.append([i, photo_num[i]])
    else:
        #print("pop!")
        min = 1000
        min_index = -10
        for j in range(len(frame_check)):
            if frame_check[j][1] < min:
                min = frame_check[j][1]
                min_index = frame_check[j][0]
             
        #print([min_index,min])        
        #print(frame_check.index([min_index,min]))
        frame_check.pop(frame_check.index([min_index,min]))    
        photo_num[min_index] = 0
        photo_num[i] += 1
        frame_check.append([i, photo_num[i]])

frame_check.sort(key=lambda x: x[0])



for i in range(len(frame_check)):
    if i < photo_frame-1:
        print(frame_check[i][0], end=" ")
    else:
        print(frame_check[i][0])    







