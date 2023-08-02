import sys, os, io, atexit
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

T = int(input())

for i in range(1,T+1):
    A, B = map(int, input().split())
    print("Case #{}: {}".format(i,A+B))