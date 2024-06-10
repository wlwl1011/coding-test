import sys, os, io, atexit
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
import copy
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def search_numbers(numbers, i, chk_nums, prime_list,N):
    
    for j in numbers:
        #print(numbers)
        num = i + j
       
        rem = numbers.replace(j, '', 1)
       
        if int(num) not in chk_nums:
            
            chk_nums.append(int(num))
            if len(num) == N:
                prime_list.append(int(num))
           
        if rem:
            search_numbers(rem, num, chk_nums, prime_list,N)

def solution(s, N):
    check_answer_list = []
    chk_nums = []
    prime_list = []
    numbers = ''
    for i in range(1,N+1):
        numbers += str(i)
    for i in numbers:
        if int(i) not in chk_nums:
            chk_nums.append(int(i))
            if len(i) == N:
                prime_list.append(int(i))
                
        rem = numbers.replace(i, '', 1)
        search_numbers(rem, i, chk_nums, prime_list,N)       
    #print(prime_list)        
    max = -1

    for index in prime_list:
        
        if s.find(str(index)) != -1 and max < index:
            
            max = index       
    
    answer =max
    
    return answer

print(solution("222", 3))