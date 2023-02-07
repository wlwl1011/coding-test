import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.reverse()

check = 0
for i in range(n):
    if k <= 0:
        break
    check += k//arr[i]
    k = k%arr[i]

print(check)    