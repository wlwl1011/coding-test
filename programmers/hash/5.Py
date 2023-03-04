def solution(genres, plays):
    
    answer = []
    dictionary = {}
    dictionary_category = {}

    for i in range(len(genres)):
        #각각을 객체로 만들어서 중복이 허용되도록 합니다.
        #장르별로 어떤 장르가 가장 많은지 기억합니다.
        if genres[i] in dictionary_category:
            dictionary[genres[i]].append([plays[i],i])
            dictionary_category[genres[i]] += plays[i]
        else:
            dictionary[genres[i]] = [[plays[i],i]]
            dictionary_category[genres[i]] = plays[i]
    
    # dictionary_category에는 value 값에 해당 장르의 총 재생 횟수가 들어가 있고 이를 내림차순 정렬합니다.
    dictionary_category = sorted(dictionary_category.items(), key=lambda x: x[1], reverse=True)

    for item_key in dictionary_category:
        count = 1 
           
        temp = sorted(dictionary[item_key[0]],key=lambda x: (-x[0],x[1]))
        for key in temp:
                if count > 2:
                    break
                else:
                    answer.append(key[1])
                    count = count + 1
    
    
    return answer