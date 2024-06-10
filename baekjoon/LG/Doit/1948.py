import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
node = [[] for _ in range(n)]
reserved = [[] for _ in range(n)]
check = [0 for _ in range(n)]

for i in range(m):
    s, e, t = map(int, input().split())
    s-= 1
    e -= 1
    node[s].append((e,t))
    reserved[e].append((s,t))
    check[e] += 1

start, end = map(int,input().split())
start -=1
end -= 1

queue = deque()
result = [0 for _ in range(n)]
queue.appendleft(start)

while queue:
    index = queue.popleft()
    for (a,t) in node[index]:
        check[a] -= 1
        result[a] = max(result[a], result[index] + t)
        if check[a] == 0:
            queue.append(a)



print(result[end])

queue = deque()
queue.append(end)
cnt = 0
visited = [False for _ in range(n)]
visited[end] = True
while queue:
    index = queue.popleft()
    for (a,t) in reserved[index]:
        if result[index] == result[a] + t:
            cnt += 1
            if not visited[a]:
                queue.append(a)
                visited[a] = True
print(cnt)




