

def solution(participant, completion):
    
    dictionary = {}

    for i in participant:
        if i in dictionary :
            dictionary[i] = dictionary[i] + 1
        else:
            dictionary[i] = 1

    for i in completion:
        if dictionary[i] <= 1:
            dictionary.pop(i)
        else:
            dictionary[i] = dictionary[i] - 1
                
    for key in dictionary.keys():
        answer = key
    return answer




