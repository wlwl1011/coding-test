def solution(priorities, location):

    answer = 0
    index = 0
    
    while(1):
        #print("priorities : ",priorities)
        #print("location : ",location)
        if priorities[index] >= max(priorities) :
            answer += 1
            if index == location:
                break
            else:    
                priorities.pop(0)
                location -= 1 
                if location < 0 :
                    location = len(priorities)-1
            
        else:
            #print("pop!")
            temp = priorities.pop(0)
            priorities.append(temp)
            location -= 1 
            if location < 0 :
                location = len(priorities)-1
                 
        

    return answer

print(solution([2,3,3,2,9,3,3], 3))
