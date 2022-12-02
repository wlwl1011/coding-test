from collections import deque 

import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))


n = int(input())
dq = deque() 
for i in range(n):
    temp = []
    temp = input()

    if len(temp) == 2:

        command = temp[0]
        data = temp[1]
        if command=="push_front":
            dq.appendleft(int(data))
        elif command=="push_back":
            dq.append(int(data))

    else:

        command = temp[0]

        if command=="size":
            print(len(dq))
        elif  command=="pop_front":  
            if len(dq) == 0:
                print(-1)   
            else:
                print(dq.popleft())
        elif  command=="pop_back":
            if len(dq) == 0:
                print(-1)   
            else:
                print(dq.remove())
        elif command=="empty":
            if len(dq) == 0:
                print(-1)   
            else:  
                print(0)
        elif command=="front":
            if len(dq) == 0:
                print(-1)   
            else:  
                print(dq[0])
        elif command=="back": 
            if len(dq) == 0:
                print(-1)   
            else:  
                print(dq[len(dq)-1])           

    


