import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N

for i in range(1,N):
    for j in range(i): #i를 가장 작은 원소로 잡는다.
        if A[j] > A[i]: #감소하는 관계이면, 이미 감소하는 관계를 만족한 것에다가 + 1
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))



