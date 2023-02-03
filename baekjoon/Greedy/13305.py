import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

#도시 개수
n = int(sys.stdin.readline())

#도로의 길이
road = list(map(int, sys.stdin.readline().split()))

#주유소 리터 당 가격
oil = list(map(int, sys.stdin.readline().split()))

#기름 값
money = oil[0]
cost = 0
for i in range(n-1):
    if money > oil[i]:
        money = oil[i]
    cost = cost + money * road[i]    

print(cost)    


    
