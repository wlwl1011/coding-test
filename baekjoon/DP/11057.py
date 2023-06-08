import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())

d = [1] * 10

for i in range(1,n):
    for j in range(1,10):
        d[j] +=d[j-1]

print(sum(d)%10007)        

