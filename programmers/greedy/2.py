def solution(name):
    
    alpabet_1 = "ABCDEFGHIJKLM"
    alpabet_2 = "NOPQRSTUVWXYZ"
    dic = {}
    answer_1 = 0
    answer_2 = 0
    answer = 0
    index = 0

    for i in alpabet_1:
        dic[i] = index
        index += 1
    index = 13
    for i in alpabet_2:
        dic[i] = index    
        index -=1
    for i in name:
        
        answer_2 += dic[i]
        answer_1 += dic[i]
        if  name.index(i) != len(name) - 1 :
            answer_2 +=1
    behind = ''    
    name = list(list(name))
    for i in range(len(name)-1,len(name)//2 ,-1 ):
        behind += str(name[i])
        name.pop()
    front = ''    
    for i in name:
        front += str(i)
    print(front)    
    print(behind)   
    name = str(name)
    for alpa in front:
        if  front.index(alpa) != len(front) - 1 :
            print("호이짜")
            answer_1 +=1
            
    answer_1 +=1
    for alpa in behind:
        
        if  behind.index(alpa) != len(behind) - 1 :
            print("호이짜")
            print("휴쪄쪄")
            answer_1 +=2
    print(answer_1)  
    print(answer_2)           
    answer = min(answer_1,answer_2)
    return answer


print(solution("LABLPAJM"))