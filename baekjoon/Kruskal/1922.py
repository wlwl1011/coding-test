import sys, os, io, atexit
import copy
from collections import deque
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))


#특정 원소가 속한 집합 찾기
def find_parent(parent,x):
    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v = int(input())
e = int(input())

parent = [0] * (v+1) #부모 테이블 초기화

#모든 간선을 담을 리스트와 최종 비용을 담을 변수

edges = []
result = 0

#부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

#모든 간선에 대한 정보 받기
for i in range(e):
    a, b, cost = map(int, input().split())
    #비용 순으로 정렬하기 위해서 튜플의 첫번째 원소를 비용으로 설정
    edges.append((cost, a, b))

#간선을 비용순으로 정렬
edges.sort()

#간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    #사이클이 발생하지 않을 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent, a, b)
        result += cost

print(result)





