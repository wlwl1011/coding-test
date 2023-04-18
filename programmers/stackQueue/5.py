from collections import deque

def solution(prices):
    answer = []
    prices_queue = deque(prices)
    while len(prices_queue) != 0:
        count = 0
        temp = prices_queue.popleft()
        for i in prices_queue:
            count += 1
            if temp > i:
                break
            
        answer.append(count)

    return answer