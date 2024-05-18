N, K = map(int, input().split())

arr = list(map(int, input()))

s = []
cnt = 0
flag = False
for i in range(N):
    while s and s[-1] < arr[i] and flag == False:
        s.pop()
        cnt += 1
        if cnt == K:
            flag = True
            break
    s.append(arr[i])
print(*s,sep='')