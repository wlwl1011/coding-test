from collections import deque

N, L = map(int, input().split())

arr = list(map(int,input().split()))
queue = deque()

for i in range(N):
    if len(queue) == 0:
        queue.append((i,arr[i]))
    else:
        if queue[-1][0] - queue[0][0] == L - 1:
            queue.popleft() 
        while queue and queue[-1][1] > arr[i]:
            queue.pop()
        queue.append((i,arr[i]))
    print(queue[0][1], end=" ")
