import sys, os, io, atexit
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    temp = arr.copy()
    first_index = 0
    last_index = n-1
    for index in range(n):
        if index % 2 == 0:
            temp[first_index] = arr[index]
            first_index +=1
        else:
            temp[last_index] = arr[index]   
            last_index -= 1
    #print(temp)        
    dif = temp[n-1] - temp[0]        
    for index in range(n-1): 
        check = temp[index+1] - temp[index]
        if check <0 :
            check = -(check)
        if dif < check:
            dif = check           



    print(dif)         
        

