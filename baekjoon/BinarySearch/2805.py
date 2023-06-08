import sys, os, io, atexit
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

tree_num, tree_length = map(int, input().split())
arr = list(map(int, input().split()))


start = 0
end = max(arr)
result = 0
while start<=end:
    mid = (start+end)//2
    sum = 0
    for i in arr:
        if i>mid:
            sum += i-mid
    if sum < tree_length:
        end = mid - 1

    else:
        result = mid
        start = mid + 1
        
print(result)            