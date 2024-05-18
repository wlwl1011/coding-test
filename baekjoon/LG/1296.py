name = list(map(str,input()))
N = int(input())
s = 0
answer = []
our_dictionary = {  'L' : 0,
                'O' : 0,
                'V' : 0,
                'E' : 0
                }

for i in range(len(name)):
    if name[i] in our_dictionary:
        our_dictionary[name[i]] += 1

for i in range(N):
    other_dictionary = {  'L' : 0,
                'O' : 0,
                'V' : 0,
                'E' : 0
                }
    other_name = input()
    for i in range(len(other_name)):
        if other_name[i] in other_dictionary:
            other_dictionary[other_name[i]] += 1
    # print(other_dictionary)
    L = our_dictionary['L']+other_dictionary['L']
    O = our_dictionary['O']+other_dictionary['O']        
    V = our_dictionary['V']+other_dictionary['V']
    E = our_dictionary['E']+other_dictionary['E']
    
    answer.append( [((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100, other_name])
    
answer.sort(key = lambda x : (-x[0],x[1]))        
print(answer[0][1])

# print(dictionary)

# for i in range(N):
    
    
    
