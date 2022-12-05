import sys, os, io, atexit
from collections import deque 

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))


n, k = map(int, input().split())
dq = deque() 

for i in range(1,n+1):
    dq.append(i)


s="<"

while len(dq) != 1:
    dq.rotate(-k+1)
    s+=str(dq.popleft()) + ', '


s+=str(dq.popleft()) + '>'
print(s)
