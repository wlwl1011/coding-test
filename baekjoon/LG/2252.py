import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

node = [[] for _ in range(N)]
check = [0 for _ in range(N)]

for _ in range(M):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    node[u].append(v)
    check[v] += 1

queue = deque()
answer = []
for i in range(N):
    if check[i] == 0:
        queue.append(i)
        check[i] = -1

while queue:
    index = queue.popleft()
    answer.append(index)
    for a in node[index]:
        if check[a] > 0:
            check[a] -= 1
            if check[a] == 0:
                queue.append(a)
                check[a] = -1
for i in range(N):
    print(answer[i]+1,end=' ')


