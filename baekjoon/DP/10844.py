import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())

d = [[0 for i in range(10)] for j in range(101)]

for i in range(1,10):
    d[1][i] = 1

for i in range(2,n+1):
    for j in range(0,10):
        if j == 0:
            d[i][j] = d[i-1][1]
        elif j == 9:
            d[i][j] = d[i-1][8]
        else:
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]        
   
print(sum(d[n])%1000000000)
