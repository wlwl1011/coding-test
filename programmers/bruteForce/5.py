
answer = 0
def dfs(k, cnt, dungeons, ch):
    global answer
    answer = max(answer, cnt)
    for i in range(len(dungeons)):
        if ch[i] == 0 and k>=dungeons[i][0]:
            ch[i] = 1
            dfs(k-dungeons[i][1],cnt+1,dungeons,ch)
            ch[i] = 0
def solution(k, dungeons):
    ch = [0]*len(dungeons)
    dfs(k,0,dungeons,ch)
    return answer

print(solution(40,[[40, 20], [10, 10], [10, 10], [10, 10], [10, 10]]))
