from collections import deque 

import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))



n = int(input())
arrN = list(map(int, input().split()))

#빠른 탐색을 위해 이를 딕셔너리에 저장함

dicN = {}

for i in arrN:
    if i in dicN:
        dicN[i] =  dicN[i] + 1
    else:    
        dicN[i] = 1

m = int(input())
arrM = list(map(int, input().split()))
s = ""
for i, idx in enumerate(arrM):

    if i != m-1 :
        if idx in dicN:
            s +=str(dicN[idx]) + " "
        else:
            s +=str(0) + " "
    else:
        if idx in dicN:
            s +=str(dicN[idx])
        else:
            s +=str(0)     

print(s)

