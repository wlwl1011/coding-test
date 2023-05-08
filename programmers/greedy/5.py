import heapq
import collections

#프림알고리즘
def prim(graph, start_node,visited):
    visited[start_node] = 1 #방문갱신
    candidate = graph[start_node]#인접간선추출
    heapq.heapify(candidate)#우선순위큐생성
    mst = []#mst
    total_weight = 0
    
    while candidate:
        weight, u, v = heapq.heappop(candidate)#가중치가 가장적은 간선 추출
        if visited[v] == 0: #방문하지 않았다면
            visited[v] = 1#방문갱신
            mst.append((u,v))#mst 삽입
            total_weight += weight
            
            for edge in graph[v]:#다음 인접 간선 탐색
                if visited[edge[2]] == 0: #방문한 노드가 아니라면
                    heapq.heappush(candidate,edge)
    return  total_weight

def solution(n, costs):
    graph = collections.defaultdict(list)
    visited = [0] * (n+1)
    
    # 무방향 그래프 생성
    for i in costs:
        u = i[0]
        v = i[1]
        weight = i[2]
        graph[u].append([weight, u, v])
        graph[v].append([weight, v, u])
        
    
    answer = prim(graph, costs[0][1] ,visited)
    return answer


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))