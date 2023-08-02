import sys, io, os, atexit
input = sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))


A, B = map(int, input().split())
if A > B:
    print('A')
elif A < B:
    print('B')
else:
    print('same')        