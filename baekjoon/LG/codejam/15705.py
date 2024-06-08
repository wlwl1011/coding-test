import sys
input = sys.stdin.readline

S = input().rstrip()
N, M = map(int, input().split())
arr = []

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

def check(i,j,dir,idx):
    while True:
        if idx >= len(S):
            break
        tx = i + dx[dir]
        ty = j + dy[dir]
        
        if 0 <= tx < N and 0 <= ty < M:
            if S[idx] == arr[tx][ty]:
                idx += 1
                if idx == len(S):
                    return True
                i = tx
                j = ty
            else:
                break
        else:
            break
    return False

for _ in range(N):
    arr.append(list(map(str,input().rstrip())))

answer = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == S[0]:
            if len(S) == 1:
                answer = 1
                break
            #첫 자가 같으므로 비교를 시작한다.
            for k in range(8):
                if check(i,j,k,1):
                    answer = 1
                if answer:
                    break
        if answer:
            break
    if answer:
        break

print(answer)
            
            

