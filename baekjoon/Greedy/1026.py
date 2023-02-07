import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
s = 0

for i in range(n):
    max = 0
    
    for k in range(n-i):
        
        if max < b[k]:
            max = b[k]
    s += max * a[i]
    b.remove(max)

print(s)
