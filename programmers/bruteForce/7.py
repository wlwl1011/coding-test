def search_words(words, i, chk_words):
    for j in words:
        word = i + j
        if len(word) <=5:
            if word not in chk_words: 
                chk_words.append(word)
                search_words(words,word,chk_words)
        else:
            return        
        
           

def solution(word):
    answer = 0
    chk_word = []
    dictionary = 'AEIOU'
    for i in dictionary:
        if i not in chk_word:
            chk_word.append(i)
            if i == word:
                break
        search_words(dictionary,i,chk_word)
    answer = chk_word.index(word)  + 1          
    return answer

print(solution("AAAAE"))