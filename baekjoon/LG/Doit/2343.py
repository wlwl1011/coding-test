import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

arr = list(map(int, input().split()))
start = max(arr)
end = sum(arr)

global answer

def isAnswer(number):
    
    check = 0
    cnt = 1
    for i in range(N-1,-1,-1):
        if check + arr[i] <= number:
            check += arr[i]
        else:
            # print("check:",check)
            check = arr[i]
            cnt += 1
    return cnt
        
def binarySearch(start, end):
    if start > end:
        return
    global answer
    
    mid = (start + end) // 2
    # print("mid:",mid)
    cnt = isAnswer(mid)
    # print("cnt:",cnt)

    if cnt <= M:
        if mid < answer:
            answer = mid
        binarySearch(start, mid-1 ) # 더 작은거 찾아봐라
       
    else:
        binarySearch(mid+1 , end)
    
        
    
    

answer = int(1e9)


binarySearch(start, end)
print(answer)