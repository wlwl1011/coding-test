import sys, os, io, atexit
from collections import deque
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())

arr = [[0 for i in range(2)] for j in range(n)]

for i in range(n):
    x, y = map(int,input().split())
    arr[i][0] = x
    arr[i][1] = y

arr = sorted(arr, key=lambda x: ( x[1],x[0])) 

for i in range(n):
    print(arr[i][0], arr[i][1])