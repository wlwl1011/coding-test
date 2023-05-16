import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
arr = []

arr_answer = [[0]*5 for i in range(n)]

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(len(arr)):
    for j in range(i+1, n):
        if arr[i][0] == arr[j][0]:
            arr_answer[i][0] += 1
            arr_answer[j][0] += 1
        elif arr[i][1] == arr[j][1]:
            arr_answer[i][1] += 1
            arr_answer[j][1] += 1  
        elif arr[i][2] == arr[j][2]:
            arr_answer[i][2] += 1
            arr_answer[j][2] += 1     
        elif arr[i][3] == arr[j][3]:
            arr_answer[i][3] += 1
            arr_answer[j][3] += 1     
        elif arr[i][4] == arr[j][4]:
            arr_answer[i][4] += 1 
            arr_answer[j][4] += 1           

sum_max = 0
index = 0
answer = 0
for i in arr_answer:
    index +=1
    if sum(i) >sum_max:
        sum_max = sum(i)
        answer = index
        
#print(arr_answer)

print(answer)    
