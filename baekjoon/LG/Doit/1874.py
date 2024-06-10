import sys
input = sys.stdin.readline

N = int(input())
stack = []
answer = []
cnt = 1
flag = False
for i in range(N):
    a = int(input())
    # print("a:",a)
    # print("stack:",stack)
    # print("answer:",answer)
    if stack and stack[-1] == a:
        stack.pop()
        answer.append('-')
    elif stack and stack[-1] > a:
        flag = True

    else:
        while cnt <= a:
            stack.append(cnt)
            cnt += 1
            answer.append('+')
            if stack and stack[-1] == a:
                stack.pop()
                answer.append('-')
if flag:
    print("NO")
else:
    for i in range(len(answer)):
        print(answer[i])