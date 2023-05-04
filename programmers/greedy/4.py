from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    dq = deque(people)
    front = 0
    behind =0
    while dq:
        #print("전",dq)
        answer +=1
        sum = 0
        if len(dq) != 0 and behind ==0:    
            behind = dq.pop()
        if len(dq) != 0 and front ==0:
            front = dq.popleft()
        #print('behind',behind)
        #print('front',front)
        if behind < limit:
            sum += behind
            behind = 0
            #print("sum += behind",sum)
            if sum + front <= limit:
                sum += front
                front = 0
                #print("sum += front",sum)
                if sum < limit:
                    while dq:
                        #print(dq)
                        if len(dq) != 0 and front == 0:
                            front = dq.popleft()
                        if sum > limit :
                            dq.appendleft(front)
                            break 
                        else:     
                            sum += front
                            front = 0         
            else:
                dq.appendleft(front)
                front = 0                        
        #print("후",dq)
    return answer 

print(solution(	[70, 50, 80, 50],100))