
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
S = [0 for _ in range(N+1)]

for i in range(1,N+1):
    S[i] = S[i-1] + arr[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(S[j]-S[i-1])