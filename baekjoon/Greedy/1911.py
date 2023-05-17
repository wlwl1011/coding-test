import sys, os, io, atexit
import math
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n , l = map(int,input().split())
arr = []
for _ in range(n):
    temp = list(map(int,input().split()))
    arr.append(temp)

arr.sort(reverse=True)   

start = 0
end = 0
answer = 0

while arr:
    s, e = arr.pop()
    if start == 0 and end == 0:
        start = s
        end = e
    else:
        if start <= s and e <= end:
            continue
        elif s <= end or s== end+1 :
            end = e
            
        else:
            answer += math.ceil((end-start)/l)
            start = s
            end = e
    if len(arr) == 0:
        answer += math.ceil((end-start)/l)        
            
   
print(answer)


