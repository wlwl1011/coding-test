import sys, os, io, atexit
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
import copy
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))


def dfs(node, arr, depth,limit,sum, count):
    if depth > limit:
        return
    for i in arr[node]:    
        sum += 10
        count += 1
        dfs(i, arr, depth + 1, limit ,sum, count)    


def solution(relationships, target, limit):
    arr = [ [] for i in range(100)]
    # visited = [ [0] * 100 for _ in range(100)]
    for i,j in relationships:
        arr[i].append(j)
        arr[j].append(i)
    sum = 0    
    count = 0
    for i in arr[target]:
        sum += 5
        count += 1
        dfs(i, arr, 1, limit, sum, count )      

    print(sum)
    print(count)
    answer = sum + count
    return answer

print(solution([[1,2],[2,3],[2,6],[3,4],[4,5]],2,3))