import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))


t = int(input()) #테스트 케이스 갯수
arr = []

for i in range(t):
    arr = list(map(int,input())) #1 아웃, 0 인
    arr_len = len(arr)
    flag = True
    for i in range(arr_len):
        if i == arr_len-1-i:
            break
        if arr[i] == arr[arr_len-1-i]:
            flag = False
            break
    if flag == True:
        print("YES")
    else:
        print("NO")    

