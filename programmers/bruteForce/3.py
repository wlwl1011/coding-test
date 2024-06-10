# def chk_prime(number):
#     if number == 0 or number == 1:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True

def search_numbers(numbers, i, chk_nums, prime_list):
    print("in search_number fuction")
    #print("numbers : ",numbers)
    #print("i : ",i)
    for j in numbers:
        print(numbers)
        num = i + j
        #print("i+j : ",i,"+",j ,"=",num)
        rem = numbers.replace(j, '', 1)
        #print("rem in search_numbers",rem)
        if int(num) not in chk_nums:
            print(num)
            chk_nums.append(int(num))
            # if chk_prime(int(num)):
            prime_list.append(int(num))
            #print("chk_nums",chk_nums)
            #print("prime_list", prime_list)      
        if rem:
            #print("again----")
            search_numbers(rem, num, chk_nums, prime_list)

def solution(numbers):
    chk_nums = []
    prime_list = []
    answer = 0
    for i in numbers:
        print(i)
        if int(i) not in chk_nums:
            chk_nums.append(int(i))
            # if chk_prime(int(i)):
            prime_list.append(int(i))
            # print("chk_nums",chk_nums)
            #print("prime_list", prime_list)       
        rem = numbers.replace(i, '', 1)
        search_numbers(rem, i, chk_nums, prime_list)
    # answer = len(prime_list)
    return answer

print(solution("171"))