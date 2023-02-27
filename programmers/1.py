def solution(nums):
    dictionary = {}
    for i in nums:
        if i in dictionary:
            dictionary[i] = dictionary[i] + 1
        else:
             dictionary[i] = 1
        
        
    answer = 0
    if len(nums) // 2 < len(dictionary):
        answer = len(nums)//2
    else:
        answer = len(dictionary)     
    return answer