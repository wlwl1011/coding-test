import sys, os, io, atexit
from collections import deque
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

computer_n = int(input())
arr = []
check_list = [0] * (computer_n+1)
for i in range(computer_n+1):
    arr.append([])

input_n = int(input())

for i in range(input_n):
    node1, node2 = map(int, input().split())
    arr[node1].append(node2)
    arr[node2].append(node1)

queue = deque()

queue.append(1)

count = 0

while queue:
    index = queue.popleft()
    if not check_list[index] :
        count +=1
        check_list[index] = 1    
        arr_list = arr[index]
        for i in arr_list:
            queue.append(i)

print(count-1)