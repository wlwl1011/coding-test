import sys, os, io, atexit
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

check_ascending = [ i for i in range(1,9)]
check_decending = [ i for i in range(8,0,-1)]
arr = [0 for _ in range(8)]

arr = list(map(int, input().split()))

if arr == check_ascending:
    print("ascending")
elif arr == check_decending:
    print("descending")
else:
    print("mixed")    