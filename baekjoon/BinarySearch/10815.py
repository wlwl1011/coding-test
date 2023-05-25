import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())

arr = set(map(int,input().split()))

m = int(input())

check_arr = list(map(int,input().split()))

for i in range(len(check_arr)):
    if i != len(check_arr)-1:
        if check_arr[i] in arr:
            print(1, end=' ')
        else:
            print(0, end=' ')    
    else:
        if check_arr[i] in arr:
            print(1)
        else:
            print(0)    
