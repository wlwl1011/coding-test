from collections import deque 

import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())

if n == 1:
    print(1)

else:
    dq = deque() 
    for i in range(1, n+1):
        dq.append(i)


    for i in range(n):
        idx =  dq.popleft()
        if len(dq)== 1:
            break
  
        idx = dq.popleft()
        dq.append(idx)
    print(dq.pop())

    