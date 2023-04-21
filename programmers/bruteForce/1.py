def solution(sizes):
    answer = 0
    max_value = []
    min_value = []
    
    #가로
    for i in sizes:
        max_value.append(max(i))
        min_value.append(min(i))

    answer = max(max_value) * max(min_value)   
    
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))