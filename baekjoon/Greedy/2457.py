import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input()) #선택한 꽃들의 최소 개수
mon = []

for i in range(n):
    start_month, start_day, end_month, end_day = list(map(int, input().split()))
    mon.append([start_month*100 + start_day, end_month*100+end_day])

mon.sort()
  
target = 301
end = 0
count = 0

while mon:
    if target >= 1201 or mon[0][0] > target:
        break

    for i in range(len(mon)):
        if target >= mon[0][0]:
            if end <= mon[0][1]:
                end = mon[0][1]
            mon.remove(mon[0])   
        else:
            break    
    target = end
    count +=1

if target < 1201:
    print(0)
else:                
    print(count)    