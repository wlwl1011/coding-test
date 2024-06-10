import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a
    
def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]



N = int(input())
M = int(input())

parent = [i for i in range(N)]
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            union(i,j)

check = list(map(int,input().split()))

temp = find(check[0]-1)
flag= True
for i in range(M):
    if find(check[i]-1) != temp:
        flag = False
if flag:
    print("YES")
else:
    print("NO")