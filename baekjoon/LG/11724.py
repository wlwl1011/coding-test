import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
answer = 0
gragh = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    gragh[a-1].append(b-1)
    gragh[b-1].append(a-1)


visited = [False for _ in range(N)]


def dfs(idx):
    visited[idx] = True
    for i in gragh[idx]:
        if not visited[i]:
            dfs(i)


for i in range(N):
    if not visited[i]:
        answer += 1
        dfs(i)

print(answer)



    
    

