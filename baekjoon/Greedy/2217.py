import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())

arr = [0 for _ in range(n)]

for i in range(n):
    arr[i] = int(input())


arr.sort(reverse=True)
answer = 0
while arr:
    if  arr[n-1] * n > answer :
        answer = arr[n-1] * n
    arr.pop()
    n -=1

print(answer)

