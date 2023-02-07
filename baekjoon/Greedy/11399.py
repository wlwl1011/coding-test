import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
s = 0

arr = list(map(int, input().split()))

arr.sort()

for i in range(n):
    for k in range(i+1):
        s += arr[k]

print(s)        