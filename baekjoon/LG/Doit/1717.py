import sys
input = sys.stdin.readline

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
    
def checkSame(a,b):
    a = find(a)
    b = find(b)

    if a==b:
        return True
    else:
        return False

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

for _ in range(m):
    operand, a, b = map(int, input().split())

    if operand == 0:
        union(a,b)
        
    else:
        if checkSame(a,b):
            print("YES")
        else:
            print("NO")

