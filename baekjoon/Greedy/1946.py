import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

test_n = int(sys.stdin.readline())

#테스트 게이스 수만큼 반복

for k in range(test_n):
    test_result = 1
    n = int(sys.stdin.readline())
    arr = []
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    
    arr.sort(key=lambda x:x[0])

    rank = arr[0][1]

    for i in range(n):
        if rank>arr[i][1]:
            rank = arr[i][1]
            test_result = test_result + 1
          

    print(test_result)