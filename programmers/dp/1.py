def solution(N, number):
    if N == number:
        return 1
    #set * 8 초기화
    s = [ set() for x in range(8)]
    
    #각 set에 N을 i번 사용했을 때 N이 i번 연속되는 기본 수 넣기
    for i,x in enumerate(s,start=1):
        x.add(int(str(N)*i))

    # {
    # "N" * i 
    #     U
    # 1번 set 사칙연산 n-1번 set 
    #     U
    # 2번 set 사칙연산 n-2번 set
    #     U
    #...
    # n-1번 set 사칙연산 1번 set
    # }

    for i in range(1, 8):
        #print("i=",i)
        for j in range(i):
            #print("j=",j)
            for op1 in s[j]:
                #print("This is op1 : ","s[",j,"]","=",op1)
                for op2 in s[i-j-1]:
                    #print("This is op2 : ","s[",i-j-1,"]","=",op2)
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        #print("s[" ,i,"]=",s[i])                

        if number in s[i]:
            answer = i + 1
            return answer
        
    return -1

print(solution(5, 12))