import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

a, b = map(int,input().split())
check = 1


while(1):

    if b<=a:
        break
    if b % 2 ==0:
        b = b//2
    else:
        temp = str(b)
        temp = list(temp)
        flag = temp.pop()
        if flag != '1':
            break
        temp = ''.join(temp)
        b = int(temp)
      
    check += 1    

if b == a:
    print(check)
else:
    print(-1)    
            