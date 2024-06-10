import sys
input = sys.stdin.readline

N, M = map(int, input().split())
answer = 0
arr = [0] + list(map(int, input().split()))

S = [0 for _ in range(N+1)]

for i in range(1,N+1):
    S[i] = S[i-1] + arr[i]
    
check = [0 for _ in range(M)]
for i in range(1,N+1):
    S[i] = S[i]%M
    check[S[i]] += 1

answer += check[0]

for i in range(M):
    if check[i] > 1:
        answer += (check[i]*(check[i]-1) // 2)

print(answer)

