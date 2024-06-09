import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

towers = []

for die in arr:
    placed = False
    for i in range(len(towers)):
        if towers[i] <= die:
            towers[i] += 1
            placed = True
            break
    if not placed:
        towers.append(1)

print(len(towers))
