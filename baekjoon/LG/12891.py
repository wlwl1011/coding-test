import sys
input = sys.stdin.readline

S, P = map(int, input().split())

arr = input().strip()

A,C,G,T = map(int,input().split())
origin = {'A':A,'C':C,'G':G,'T':T}
start = 0
end = 0
answer = 0 
check = {'A':0,'C':0,'G':0,'T':0}
check[arr[0]] += 1
while end < S:
    if end - start >= P-1:
        if end - start == P-1:
            flag = True
            for key, value in origin.items():
                if check[key] < origin[key]:
                    flag = False
            if flag:
                answer += 1
        check[arr[start]] -= 1
        start += 1
      
    else:
        end += 1
        if end >= S:
            break
        check[arr[end]] += 1
    # print(start, end, check)
print(answer)