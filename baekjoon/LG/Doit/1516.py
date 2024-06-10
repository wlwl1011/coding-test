import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
node = [[] for _ in range(N)]
time = [0 for _ in range(N)]
check = [0 for _ in range(N)]

# 건물 정보를 입력받습니다.
for i in range(N):
    temp = list(map(int, input().rstrip().split()))
    time[i] = temp[0]
    for j in range(1, len(temp) - 1):
        node[temp[j] - 1].append(i)
        check[i] += 1

queue = deque()
answer = time[:]

# 진입 차수가 0인 노드를 큐에 넣습니다.
for i in range(N):
    if check[i] == 0:
        queue.append(i)

while queue:
    index = queue.popleft()
    for a in node[index]:
        check[a] -= 1
        answer[a] = max(answer[a], answer[index] + time[a])
        if check[a] == 0:
            queue.append(a)

# 각 건물의 최소 건설 시간을 출력합니다.
for i in range(N):
    print(answer[i])
