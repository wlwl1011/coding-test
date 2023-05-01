def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    for i in range(1, n+1):
        if i in lost and i in reserve:
            answer +=1
        elif i in lost:
            if i-1 in reserve and i+1>=0  and i-1 not in lost:
                answer += 1
                index = reserve.index(i-1)
                reserve.pop(index)   
            elif i+1 in reserve and i+1<=n and i+1 not in lost:
                answer+= 1
                index = reserve.index(i+1)
                reserve.pop(index)
            
        else:
            answer +=1
                
    return answer


print(solution(6, [6, 2, 4], [1, 5, 3]))