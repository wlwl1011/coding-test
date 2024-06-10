import sys
input = sys.stdin.readline

N = int(input())



start = 1
end = 1
sum = 0
answer = 0

while start <= N:
    if sum < N:
        sum += end
        end += 1
        
    else:
        if sum == N:
            answer += 1
        sum -= start
        start += 1

print(answer)