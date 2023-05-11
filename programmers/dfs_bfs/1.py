def solution(numbers, target):
    leaves = [0] #모든 계산 결과를 담는 리스트
    count = 0

    for num in numbers:
        temp = []

        for leaf in leaves:
            temp.append(leaf + num) #더하는 경우
            temp.append(leaf - num) #빼는 경우
             
        leaves = temp  
        #print(leaves)  
    answer = 0

    for leaf in leaves:
        if leaf == target:
            answer +=1
    return answer

solution([4, 1, 2, 1], 2)