import sys
input = sys.stdin.readline

arr = list(map(int, input().rstrip()))

stack = []

for a in arr:
    if stack:
        if stack[-1] < a:
            stack.append(a)
        else:
            tmp = []
            while stack and stack[-1] > a:
                tmp.append(stack.pop())
            stack.append(a)
            while tmp:
                stack.append(tmp.pop())
    else:
        stack.append(a)

print(*stack[::-1], sep="")