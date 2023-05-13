import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m, k = map(int,input().split())
answer = 0

n = n//2

if n >= m:
    while(n>=m):
        if k == 0:
            break
        if k-2 >=0:
            n -=1
            k -=2
        else:
            n = n*2
            n -= 1
            k -=1
            n = n // 2    
    if k > 0:
        while(k>=0):
            if k-2>=0 and n >= m: 
                n -=1
                k -=2
            elif k-1>=0 :
                m -=0
                k -=1    
else:
    while(m>=n):
        if k == 0:
            break
        m -=1
        k -=1
    if k > 0:
        while(k>=0):
            if k-2>=0 and n >= m: 
                n -=1
                k -=2
            elif k-1>=0 :
                m -=0
                k -=1     

answer = min(n,m)


print(answer)
