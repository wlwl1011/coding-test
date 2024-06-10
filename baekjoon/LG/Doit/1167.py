import sys
input = sys.stdin.readline
from collections import deque

def bfs(n):
    visited = [False for _ in range(V)]
    queue = deque()
    visited[n] = True
    queue.append((n, 0))

    farthest_node = n
    max_length = 0

    while queue:
        x, length = queue.popleft()
        if length > max_length:
            max_length = length
            farthest_node = x

        for (v, l) in tree[x]:
            if not visited[v]:
                visited[v] = True
                queue.append((v, length + l))

    return farthest_node, max_length

V = int(input())
tree = [[] for _ in range(V)]

for _ in range(V):
    temp = deque(list(map(int, input().rstrip().split())))
    v = temp.popleft()
    
    while temp[0] != -1:
        v2 = temp.popleft()
        length = temp.popleft()
        tree[v-1].append((v2-1, length))

# Step 1: Perform BFS from an arbitrary node to find the farthest node A
start_node = 0
farthest_node, _ = bfs(start_node)

# Step 2: Perform BFS from node A to find the farthest node B and the length of the path
_, diameter = bfs(farthest_node)

print(diameter)
