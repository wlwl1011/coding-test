import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
arr = []

arr_answer =  [[] for i in range(n)]

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(i+1, n):
        if i == j:
            continue
        if arr[i][0] == arr[j][0]:
            if j not in arr_answer[i]:
                arr_answer[i].append(j)
            if i not in arr_answer[j]:
                arr_answer[j].append(i)    
        elif arr[i][1] == arr[j][1]:
            if j not in arr_answer[i]:
                arr_answer[i].append(j)
            if i not in arr_answer[j]:
                arr_answer[j].append(i)    
        elif arr[i][2] == arr[j][2]:
            if j not in arr_answer[i]:
                arr_answer[i].append(j)
            if i not in arr_answer[j]:
                arr_answer[j].append(i)     
        elif arr[i][3] == arr[j][3]:
            if j not in arr_answer[i]:
                arr_answer[i].append(j)
            if i not in arr_answer[j]:
                arr_answer[j].append(i)   
        elif arr[i][4] == arr[j][4]:
            if j not in arr_answer[i]:
                arr_answer[i].append(j)
            if i not in arr_answer[j]:
                arr_answer[j].append(i)    
                   

len_max = 0
index = 0
answer = 1
for i in arr_answer:
    index +=1
    if len(i) >len_max:
        len_max = len(i)
        answer = index
        
#print(arr_answer)

print(answer)    
