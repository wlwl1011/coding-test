import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())

d = [0]*(n+1)
path = ["" for _ in range(n+1)] # 최단 경로
path[1] = "1"

for i in range(2,n+1):
    #현재 수에서 1을 빼는 경우    
    d[i] = d[i-1] + 1
    prev = i-1
    #3으로 나누는 경우
    if i%3 == 0 and d[i//3]+1 < d[i]:
        temp = d[i]
        d[i] = d[i//3]+1
        prev = i // 3

    #2로 나누어 떨어지는 경우
    if i%2 == 0 and d[i//2]+1 < d[i]:
        temp = d[i]
        d[i] =d[i//2]+1
        prev = i // 2

    path[i] = str(i) + " " + path[prev]    
 

   

print(d[n])
print(path[n])