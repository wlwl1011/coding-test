import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())

for i in range(n):
    total = 0
    isInvalid = False
    arr = []
    arr = input()

    for k in arr:
        if k == '(':
            total += 1
        else :
            if total == 0 :
                isInvalid = True
            else :    
                total -= 1
    if total == 0 :
        if isInvalid:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")                


