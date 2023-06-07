import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))


def check(arr):

    arr_len = len(arr)
    if arr_len==1:
        return True

    for i in range(arr_len//2):
        if arr[i] == arr[arr_len-1-i]:
            return False
    return check(arr[0:len(arr)//2]) and check(arr[len(arr)//2+1:len(rules)])
                

       



t = int(input()) #테스트 케이스 갯수

for i in range(t):
    rules = list(map(int,input())) #1 아웃, 0 인
    if check(rules):
        print("YES")
    else:
        print("NO")    
