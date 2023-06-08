import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, k = map(int, input().split())

arr = []
d = [10001]* (k+1)
for i in range(n):
    arr.append(int(input()))
d[0] = 0
for i in arr:
    for j in range(i, k+1):
        if d[j-i] != 10001:
            d[j] = min(d[j], d[j-i]+1)

if d[k] == 10001:
    print(-1)
else:
    print(d[k])    

