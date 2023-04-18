import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while(1) :
        if len(scoville)<=1 and scoville[0] < K:
            return -1
        first = heapq.heappop(scoville)
        if first>=K:
            break
        answer += 1
        second = heapq.heappop(scoville)
        new = first + ( second * 2 )
        heapq.heappush(scoville, new)
    return answer
print(solution([0,0,0,0,0], 7))