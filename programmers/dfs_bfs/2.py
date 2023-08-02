from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for node in range(n):
        queue = deque()
        if visited[node] == 0:
            queue.append(node)
            answer += 1
        while queue:
            i= queue.popleft()
            visited[i] = 1
        
            for j in range(n):
                if computers[i][j]==0:
                    continue
                if visited[j] == 0:
                    queue.append(j)
                    visited[j] = 1
    return answer
