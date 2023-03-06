def solution(arr):
    answer = []
    for index in arr:
        length = len(answer)
        if length == 0:
            answer.append(index)
        elif index != answer[length-1]:
            answer.append(index)
    
    return answer