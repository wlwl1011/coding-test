import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())


for k in range(n):
    d = int(input())
    arr = []
    arr = list(map(int, input().split()))
    max = arr[d-1]
    buy = []
    benefit = 0
    for i in range(d-1, -1, -1):
        #최대값 변경
        if arr[i]>max :
            max = arr[i]
        else:
            benefit += max - arr[i]
            buy.append(arr[i])
    print(benefit)        












