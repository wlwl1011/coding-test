answer = []
diff = []
progresses = [1, 1, 1, 1]
speeds = [100, 50, 99, 100]

for i in range(len(progresses)):
    diff.append(100-progresses[i])

for i in range(len(speeds)):
    # // 연산은 나누기 할 때 소수점 이하를 버린다 .. 이를 주의해야함 !

    #만약 나누어 떨어지지 않는 값이라면 ...
    if  diff[i]%speeds[i] != 0:
        diff[i] = diff[i]//speeds[i] + 1
    else:  
        diff[i] = diff[i]//speeds[i]   

max = 0    
cnt = 1

for i in range(len(diff)): 
    if i == 0:
        max = diff[i]
    else:
        if diff[i]<=max:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            max = diff[i]
answer.append(cnt) 
print(answer)