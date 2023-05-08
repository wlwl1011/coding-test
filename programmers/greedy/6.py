import heapq

def solution(routes):
    heapq.heapify(routes)#우선순위큐생성
    answer = 0

    while routes:
        answer +=1
        start, end = heapq.heappop(routes) #가중치가 가장적은 간선 추출
        if routes:
            start_list = routes[0]
            while start_list:
                if end >= start_list[0] and routes:
                    heapq.heappop(routes)
                    if routes:
                        start_list = routes[0]
                else:
                    break   

    return answer

print(solution(	[[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))