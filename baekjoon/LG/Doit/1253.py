import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()


cnt = 0
for idx in range(N):
    check = arr[idx]
    new_arr = []
    for a in range(N):
        if a != idx:
            new_arr.append(arr[a])
    start = 0
    end = N-2
    flag = False
    while start < end:
        if new_arr[start] + new_arr[end] <= check:
            if new_arr[start] + new_arr[end] == check:
                flag = True
                break
            start += 1
        else:
            end -=1
           
    if flag:
        cnt += 1
print(cnt)
    