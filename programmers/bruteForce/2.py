def solution(answers):
    person1= [1, 2, 3, 4, 5]
    person2= [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    check = [0 for _ in range(3)]
    answer = []
    index = 0
    for i in answers:
        if i == person1[(index)%len(person1)]:
            check[0] += 1
        if i == person2[(index)%len(person2)]:
            check[1] += 1
        if i == person3[(index)%len(person3)]:
            check[2] += 1   
        index +=1 
    max_value = max(check)
    index = 1
    for i in check:
        if i == max_value:
            answer.append(index)
        index +=1    
    return answer


print(solution([1, 3, 2, 4, 2]))