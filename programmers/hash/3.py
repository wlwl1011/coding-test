def solution(phone_book):
    answer = True
    dictionary = {}
    for phone_number in phone_book:
        dictionary[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in dictionary and temp != phone_number:
                answer = False
        
    return answer