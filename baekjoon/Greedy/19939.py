import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, k = map(int, input().split())

check = k(k+1)//2

if check > n:
    print(-1)
else :
    a = n - check 
    if a % k == 0:
        print(k-1)
    else:
        print(k)     
