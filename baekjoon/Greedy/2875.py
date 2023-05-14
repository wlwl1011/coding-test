import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

N, M, K=map(int, input().split())
team = 0
while True :
    N-=2
    M-=1
    if N<0 or M<0 or (N+M)<K:
        break
    team+=1
print(team)
