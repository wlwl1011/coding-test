
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
    for i in range(len(name)-1, 0, -1):
        behind.append(name[i])
    behind.append(name[0])

    for i in name:
        temp = 0
        #print("front", front)
        #print("behind",behind)
        temp_font = front.copy()
        temp_behind = behind.copy()
        if len(temp_font) > 0 and temp_font[len(temp_font)-1] == 'A':
            temp_font.pop()
            while 1:
                if len(temp_font) > 0 and temp_font[len(temp_font)-1] == 'A':
                    temp_font.pop()
                else:
                    break  
        if len(temp_behind) > 0 and temp_behind[len(temp_behind)-1] == 'A':
            temp_behind.pop()
            while 1:
                if len(temp_behind) > 0 and temp_behind[len(temp_behind)-1] == 'A':
                    temp_behind.pop()
                else: break    
        #print("temp_font",temp_font)
        #print("temp_behind",temp_behind)
        if len(front) >= len(behind):
            if 2*(len(temp_behind) - 1) >=0 :
                temp += 2*(len(temp_behind) - 1)
            temp += len(temp_font) - 1   

            if len(temp_behind) == 0 or len(temp_font) == 1:
                temp +=1 
            else: 
                temp +=2     
        else:
            temp += len(temp_behind) - 1
            if 2*(len(temp_font) - 1) >=0 :   
                temp += 2*(len(temp_font) - 1)

            if len(temp_font) == 0 or len(temp_behind) == 1:
                temp +=1 
            else: 
                temp +=2      
        #print("이동횟수", temp)            
        answer_list.append(answer + temp)
        #print(answer + temp)
        if len(behind) > 0:
            behind.pop()
        front.append(i)
    #print("front", front)
    #print("behind",behind)
    temp = 0
    temp += len(front) - 1  
    #print(answer + temp)
    answer_list.append(answer + temp)
    answer = min(answer_list)
    return answer


print(solution("JAN"))