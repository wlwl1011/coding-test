import sys
input = sys.stdin.readline
from collections import deque

node = list(map(int, input().split()))
queue = deque()
queue.append((0,0))

sender = [0,0,1,1,2,2]
reciever = [1,2,2,0,0,1]
visited = [[0 for _ in range(201)] for _ in range(201)]
visited[0][0] = 1
answer = []
while queue:
    # print(queue)
    now_node = queue.popleft()
    a = now_node[0]
    b = now_node[1]
    c = node[2] - (a+b)

    for idx in range(6):
        next_node = [a,b,c]
        next_node[reciever[idx]] += next_node[sender[idx]]
        next_node[sender[idx]] = 0
        if next_node[reciever[idx]] > node[reciever[idx]]:
             next_node[sender[idx]] = next_node[reciever[idx]] - node[reciever[idx]]
             next_node[reciever[idx]] = node[reciever[idx]]

        if not visited[next_node[0]][next_node[1]]:
            visited[next_node[0]][next_node[1]] = 1
            queue.append((next_node[0],next_node[1]))
            if next_node[0] == 0:
                answer.append(next_node[2])
answer.append(node[2])
answer.sort()

print(*answer)
                     
            

