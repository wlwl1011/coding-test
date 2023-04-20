import heapq

def solution(operations):
    heap = []
    answer = []
    for i in operations:
        command, number = i.split()
        number = int(number)
        if command == "I":
            heapq.heappush(heap,number)
        elif command == "D":
            if len(heap) >0:
                if number == 1:
                    #최댓값 삭제
                    heap.pop(heap.index(heapq.nlargest(1,heap)[0]))
                elif number == -1:
                   #최솟값 삭제
                   heap.pop(heap.index(heapq.nsmallest(1,heap)[0]))
    if len(heap) == 0 :
        answer = [0,0]
    else:
        max = heapq.nlargest(1,heap)[0]
        min = heapq.nsmallest(1,heap)[0]
        answer = [max, min]
    return answer


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))