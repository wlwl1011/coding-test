from collections import deque 

def solution(numbers):
    answer = ''
    split_numbers = [ "" for _ in range(len(numbers))] 
    index = 0
    for i in numbers:
        split_numbers[index] = str(i)
        index +=1
    
    split_numbers = sorted(split_numbers,key=lambda x: int(x[0]),reverse= True)     
    split_numbers = sorted(split_numbers,key=lambda x: x*3, reverse= True)   
    for i in split_numbers:
        answer += i

    if answer.startswith("0"):
        answer = "0"
    
    return answer

print(solution([3, 30, 34, 5, 9]))