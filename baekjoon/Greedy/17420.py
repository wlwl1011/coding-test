import sys
import math

read = sys.stdin.readline

n = int(read())
A = list(map(int, read().split()))
B = list(map(int, read().split()))

arr = []

for r1, r2 in zip(A, B):
    arr.append([r1, r2])

# B를 기준으로 정렬
# A를 기준으로 정렬
arr.sort(key=lambda x: (x[1], x[0]))

# 0번째 index의 B값을 p에 저장한다. (첫 번째 B값으로 A의 위치를 확인한다.)
previous = arr[0][1]
cur_max = -1
answer = 0
cnt = 0

for i in range(n):
    # 현재 Ai 값이
    # - 이전 1 ~ i - 1 구간 계산된 결과 중 최댓 값 Ai 보다 작거나
    # - 이전 1 ~ i - 1 구간의 Bi의 최댓 값보다 작을 때
    # Ai값을 갱신해줘야 한다. (30일 x t)
    # 현재 t값을 구해서 갱신하는 것이다.
    if previous > arr[i][0]:
        previous = max(previous, arr[i][1])
        # if previous < arr[i][1]:
        #     previous = arr[i][1]

        cnt = math.ceil((previous - arr[i][0]) / 30)
        arr[i][0] += cnt * 30  # 30일씩 추가해줘야한다.
        answer += cnt

    # - 이전 1 ~ i - 1 구간 계산된 결과 중 최댓 값 Ai 보다 작거나
    # - 이전 1 ~ i - 1 구간의 Bi의 최댓 값보다 작을 때
    # 이 두 구간중 가장 큰 값으로 갱신해야 한다.
    # arr[i][0]은 갱신된 상태
    cur_max = max(cur_max, arr[i][0])

    # 만약, 현재 Bi와 다음 Bi+1 값이 다르다면, 이전 값을 갱신해준다.
    # Bi와 다음 Bi+1 가 같다면, 그대로 유지한다.
    if i + 1 < n and (arr[i][1] != arr[i + 1][1]):
        previous = cur_max


print(answer)