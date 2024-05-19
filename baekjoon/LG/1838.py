import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
A = []

for i in range(N):
    A.append((arr[i],i))


Max = 0
sorted_A = sorted(A)

for i in range(N):
    if Max < sorted_A[i][1] - i:
        Max = sorted_A[i][1] - i

print(Max)