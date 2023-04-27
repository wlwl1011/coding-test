
def dfs( wires, ch, element):
    cnt = 1
    for i, ele in enumerate(wires):
        if ch[i] == 0 and element in ele:
            ch[i] = 1
            if ele[0] == element:
                cnt += dfs(wires, ch, ele[1])
            else:
                cnt += dfs(wires, ch, ele[0])
            ch[i] = 0    
    return cnt        
            
def solution(n, wires):
    answer = 10000
    ch = [0]*(n+1)
    for i in range(len(wires)):
        ch[i] = 1
        cnt_a = dfs(wires, ch, wires[i][0])
        cnt_b = dfs(wires, ch, wires[i][1])
        ch[i] = 0
        answer = min(answer, abs(cnt_a - cnt_b))    
    return answer


print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))