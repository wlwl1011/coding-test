import sys
input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    arr.append(list(map(int,input().rstrip().split())))

arr.sort(key = lambda x : (x[1],x[0]))

now_start, now_end = 0,0
cnt = 0
# print("---------")
for start, end in arr:
    if start >= now_end:
        # print(start, end)
        now_start = start
        now_end = end
        cnt += 1
print(cnt)
