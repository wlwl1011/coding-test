

def solution(clothes):
    answer = 0
    dictionary = {}
    for name, kind in clothes:
        if kind in dictionary:
            dictionary[kind] = dictionary[kind] + 1
        else:
            dictionary[kind] = 1
            
    result = 1
    for i in dictionary:
        temp = dictionary[i]
        result *= (temp+1)
        
    answer = result - 1        
    return answer