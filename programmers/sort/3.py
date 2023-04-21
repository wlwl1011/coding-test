def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    print(citations)
    for i in citations:
        answer +=1
        print(i,answer)
        if i == answer:
            break
        if i < answer:
            answer = answer - 1
            break
    return answer

print(solution([1, 4, 5]))