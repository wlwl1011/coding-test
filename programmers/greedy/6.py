import heapq

def solution(routes):
    heapq.heapify(routes)#우선순위큐생성
    answer = 0
    
    while routes:
        print(routes)
        answer +=1
        start, end = heapq.heappop(routes) #가중치가 가장적은 간선 추출
        if routes:
            start_list = routes[0]
            end_temp = end
            while start_list:
                if end >= start_list[0] and routes :
                    end_temp = min(end_temp, routes[0][1])
                    if end_temp < routes[0][0]:
                        break
                    else:
                        start1, end1 = heapq.heappop(routes)
                        if routes:
                            start_list = routes[0]
                        else: 
                            start_list = []   
                else:
                    break

    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))