N = int(input())
arr = list(map(int, input().split()))

answer = [-1 for _ in range(N)]
s = []

for i in range(N-1,-1,-1):
    while s and s[-1] <= arr[i]:
        s.pop()
    if not s:
        answer[i] = -1
    else:
        answer[i] = s[-1]
    s.append(arr[i])    


print(*answer)
