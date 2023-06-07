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
    if arr_len==1:
        print("YES")
    else:
        for i in range(0,arr_len,3):
            if i+2>=arr_len:
                break
            if arr[i] == arr[i+2]:
                flag = False
                break
        if flag == True:
            print("YES")     
        else:
            print("NO")    

