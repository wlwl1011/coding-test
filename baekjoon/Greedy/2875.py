import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m, k = map(int,input().split())
answer = 0
while True:
    if k == 0:
        break
    if n > m and k:
        n -=1
        k -=1
    elif m> n and k:
        m -=1
        k -=1
        
    if n-2>=0 and m-1 >=0:
        n-=2
        m -=1
        answer +=1

print(answer)
