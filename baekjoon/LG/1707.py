import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
isEven = True

def dfs(node):
    global isEven
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            check[i] = (check[node]+1) %2
            dfs(i)
        elif check[node] == check[i]:
            isEven = False


K = int(input())

for _ in range(K):

    V, E = map(int, input().split())
    visited = [False for _ in range(V)]
    graph = [[] for _ in range(V)]
    check = [0 for _ in range(V)]
    isEven = True
    for _ in range(E):
        a, b = map(int, input().rstrip().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    for node in range(V):
        dfs(node)   
    
    if isEven:
        print("YES")
    else:
        print("NO")