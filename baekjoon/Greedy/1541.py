import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

s = input().split('-')

#-를 기준으로 잘라서 더해주면 된다.

sum = 0
check = 0
for i in s:
  
    temp_sum = 0
    temp = map(int, i.split('+'))
    
    for index in temp:
        
        temp_sum += index
    
    if check == 0:
        sum = temp_sum
        check += 1
    else:    
        sum = sum - temp_sum            
    
print(sum)