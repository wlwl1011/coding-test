from collections import deque
import heapq

def solution(jobs):
    answer = 0
    result = []
    heap = []
    time = 0
    delay = 0
    temp_start = 0
    #시간 순으로 정렬을 시킨다.
    jobs.sort(key=lambda x:x[0])
    for arr in jobs:
        heapq.heappush(heap, [arr[1],arr[0]])
    while(1):
        #print("몇초까지 기다려야하나요",delay)
        #print(time)
        #print(heap)
        if len(heap) == 0:
            break
        #그 전의 작업이 끝났는지 확인
        
        if time >= delay:
            #해당 시간에 가능한 애들을 확인


            #일단 제일 위에꺼 읽어와!
            temp_list = heap[0]
            temp_dif = temp_list[0] # 걸리는 시간
            temp_start = temp_list[1] # 요청을 받은 시간
            if temp_start <= time :
                #print("pop!!", temp_list)
                heapq.heappop(heap)
                delay = time + temp_dif
                #print("걸리는 시간",temp_dif + (time - temp_start))
                result.append(temp_dif + (time - temp_start))
            else:
                #걸리는 시간은 크지만 남는 시간에 할 수 있는게 있나 확인
                new_heap = deque()
                count = 0
                while(heap):
                    check = heapq.heappop(heap)
                    #print("걸리는 시간은 크지만 남는 시간에 할 수 있는게 있나 확인", check)
                    if check[1] <= time :
                        count += 1
                        break
                    else:
                        new_heap.append(check)
                #그런게 있다.        
                if count != 0:        
                    #print("pop!!", check)        
                    delay = time + check[0]
                    result.append(check[0] + (time - check[1]))    
                    #print("걸리는 시간",check[0] + (time - check[1]))    
                for i in new_heap:
                    heapq.heappush(heap, i)
                #그런게 없으면 그냥 시간을 두고 기다려야하는거 아닌가?
                   

        time += 1 
    #print(result)    
    answer = sum(result) / len(result)    
    return int(answer)

print("result is",solution([[0,10],[4,10],[5,11],[15,2]]))