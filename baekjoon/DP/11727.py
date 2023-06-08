import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3,n+1):
    d[i] = (d[i-1] + d[i-2]*2)%10007

print(d[n])     