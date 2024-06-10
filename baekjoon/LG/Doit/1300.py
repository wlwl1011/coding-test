import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

start = 1
end = N*N

def countNumber(number):
    cnt = 0
    for i in range(1,N+1):
        cnt += min(N, number // i)
    return cnt

answer = 0
while start <= end:
    mid = (start + end) // 2
    check = countNumber(mid)

    if check >= k:
        end = mid - 1
        answer = mid
    else:
        
        start = mid + 1


print(answer)
