import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

arr = [[0]*101 for _ in range(101)]


#냅다 더하기
for _ in range(4):
    temp = list(map(int, input().split()))
    for i in range(temp[0], temp[2]):
        for j in range(temp[1],temp[3]):
            arr[i][j] = 1

print(sum(sum(arr,[])))


