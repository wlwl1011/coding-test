import sys, os, io, atexit
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

W, N = map(int, input().split())
arr = [[0] * 2 for i in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

arr.sort(key = lambda x:(x[1])) #기존에 x[0]도 정렬 시켜줬는데 시간초과남.

answer = 0

while True:
    
    w, m = arr.pop()

    if W - w<= 0:
        answer += W * m
        break
    W -= w
    answer += w * m 
    
print(answer)