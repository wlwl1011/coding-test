global answer_length

def dfs(number,i,answer_list ):
    #print("number", number)
    #print("i",i)
    global answer_length 
    temp = ''
    for j in number: 
        temp += j
        new_num = i + j
        if len(new_num) == answer_length :
            answer_list.append(new_num)
        elif len(new_num) <  answer_length:
            new_number =  number.replace(temp,'',1)
            dfs(new_number,new_num,answer_list )
    

def solution(number, k):
    answer_list = []
    global answer_length 
    answer_length = len(number) - k
    answer = ''
    temp_number = ''
    temp = ''
    for i in range(answer_length):
        temp_number += number[i]
    #print(temp_number)    
    for num in temp_number:  
        temp += num
        #print("호이짜 !",temp)
        if len(num) == answer_length:
            answer_list.append(num)
        elif len(num) <  answer_length:    
            new_number = number.replace(temp,'',1)
            dfs(new_number,num,answer_list )
    #print(answer_list)        
    answer = max(answer_list)    
    return answer

print(solution("1231234", 3))