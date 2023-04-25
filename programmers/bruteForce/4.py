def solution(brown, yellow):
    answer = []
    #yellow의 약수를 찾는당
    divisor = []
    for i in range(1,yellow+1):
        if yellow%i == 0 and not (yellow//i,i) in divisor:
            divisor.append((i,yellow//i))
    for index in divisor:
        width = index[0] 
        height = index[1]

        if (width+2) * (height+2) - yellow == brown:
            answer.append(index[1]+2)
            answer.append(index[0]+2)
            break
    
    return answer


print(solution(24,24))