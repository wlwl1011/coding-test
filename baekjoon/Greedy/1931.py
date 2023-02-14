import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

arr = []
n = int(input())


for i in range(n):
    #시간 값 입력
    start, end = list(map(int,input().split()))
    arr.append([start,end])


#끝나는 시간을 기준으로, 그 값이 짧은 것을 기준으로 정렬한다. 
arr.sort(key=lambda x:x[1])  
arr.sort(key=lambda x:x[0])  

check = 0
finish = 0

for i, j in arr:
    
    if i >= finish :
        check += 1
        finish = j
       
print(check)