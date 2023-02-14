import sys, os, io, atexit


input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = list(input())

sum = 0
check = 0
result = 0
index = 0
#각 자리 수를 정수 형태로 만들어줌
for i in range(len(n)):
    if n[i] == '0':
        check = 1
    sum += int(n[i])

if check != 1:
    print(-1)
elif sum % 3 != 0:
    print(-1)
else:
    n.sort(reverse=True)
    print(''.join(n))
    







