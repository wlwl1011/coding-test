import sys, os, io, atexit
import copy
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())

arr = [[0] * 4 for i in range(n)]

for i in range(n):
    arr[i] = list(map(int, input().split()))

#  (x,y) 시작점 / d 시작방향 / g 세대

