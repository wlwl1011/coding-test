arr = list(map(str, input()))
stack = []
answer = 0
for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(arr[i])
    elif arr[i] == ')':
        if arr[i-1] == '(':
            stack.pop()
            answer += len(stack)
            # print(len(stack))
        else:
            stack.pop()
            answer += 1

print(answer)

