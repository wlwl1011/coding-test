import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(int(input().rstrip()))


answer = 0
for money in arr[::-1]:
    # print("K:",K)
    if K == 0:
        break
    if K >= money:
        answer += (K // money)
        K = K % money 

print(answer)