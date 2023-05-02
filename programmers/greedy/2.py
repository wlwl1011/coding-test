
def solution(name):
    
    alpabet_1 = "ABCDEFGHIJKLM"
    alpabet_2 = "NOPQRSTUVWXYZ"
    dic = {}
    answer = 0
    answer_list = []
    index = 0
    #각 알파벳에 요구되는 조이스틱의 최소 수
    for i in alpabet_1:
        dic[i] = index
        index += 1
    index = 13
    for i in alpabet_2:
        dic[i] = index    
        index -=1
    #할당    
    for i in name:
        answer += dic[i]
    #print(answer)
    #각 알파벳의 위치에 요구되는 조이스틱의 최소 수
    #이를 하기 위해 완전 탐색해야함
    front = []
    behind = []
    front_check = []
    behind_check = []

    for i in range(len(name)-1, 0, -1):
        behind.append(name[i])
        behind_check.append('A')
    behind.append(name[0])
    behind_check.append('A')
    
    for i in name:
        temp = 0
        print("front", front)
        print("behind",behind)
        
        if len(front) >= len(behind):

            if 2*(len(behind) - 1) >=0 :
                temp += 2*(len(behind) - 1)
            temp += len(front) - 1       
            if len(behind) != 0:
                #앞뒤 왔다갔다 ..
                temp +=2         
        else:
            temp += len(behind) - 1
            if 2*(len(front) - 1) >=0 :
                temp += 2*(len(front) - 1)
            
            if len(front) != 0:
                #앞뒤 왔다갔다 ..
                temp +=2
            else: 
                temp +=1          
        answer_list.append(answer + temp)
        print(answer + temp)
        if len(behind) > 0:
            behind.pop()
            behind_check.pop()
        front.append(i)
        front.append('A')
        
    print("front", front)
    print("behind",behind)
    temp = 0
    temp += len(front) - 1  
    print(answer + temp)
    answer_list.append(answer + temp)
    answer = min(answer_list)
    return answer


print(solution("JAN"))