def solution(array, commands):
    answer = []
    for com in commands:
        splited_array = array[com[0]-1:com[1]]
        #print(splited_array)
        splited_array.sort()
        answer.append(splited_array[com[2]-1])
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))