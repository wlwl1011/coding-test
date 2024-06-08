import sys
input = sys.stdin.readline

N, K, M = map(int,input().split())

A = list(map(int, input().split()))


for _ in range(M):
    i = int(input())

    if i < 0:
        i = -i
        if K >= N-i+1 :
 
            K = N - (K - (N-i+1))
    
    else:
        if K <= i:
            K = i - K + 1
 

        

print(K)
