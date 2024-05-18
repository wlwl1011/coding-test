import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

stack = []
answer = []
for i in range(len(arr)-1,-1,-1):
    # print(i)
    a = arr[i]
    
    while stack and a >= stack[-1]:
        stack.pop()
    if stack and stack[-1] > a:
        answer.append(stack[-1])
    else:
        answer.append(-1)
    stack.append(a)
    # print(a, stack)

print(*answer[::-1])