import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

arr = [[0 for j in range(4)] for i in range(4)]
sum = 0

#냅다 더하기
for i in range(4):
    temp = list(map(int, input().split()))
    arr[i] = temp
    sum += (temp[3] - temp[1]) * (temp[2] - temp[0])

#겹쳐진거 빼야함
#print(arr)

while len(arr)>1:
    print(sum)
    check_list = []
    temp = arr.pop()
    check_list.append(temp)
    for i in arr:
        #겹치는 필요 조건
        if temp[3] >= i[1] or temp[1] <= i[3]:
            if temp[2] <= i[0] or temp[0] <= i [2]:
                #print(temp,i)
                check_list.append(i)
                #겹쳐지는 높이 구하기
                height = 0
                if temp[3] >= i[3] and temp[1] >= i[1]:
                    height = i[3] - i[1]
                elif temp[3] >= i[3]  and  i[3] >= temp[1] :
                    height =  i[3] - temp[1]
                elif i[3] >= temp[3] and temp[3] <= i[1]:
                    height = temp[3] - i[1]

                width = 0
                if temp[2] >= i[2] and temp[0] >= i[0]:
                    width = i[2] - i[0]
                elif temp[2] >= i[2]  and  i[2] >= temp[0] :
                    width =  i[2] - temp[0]
                elif i[2] >= temp[2] and temp[2] <= i[0]:
                    width = temp[2] - i[0]   
                sum -= height * width
    if len(check_list) >=3 :
        print(sum,check_list)
        height_1 = 0
        height_2 = 100
        width_1 = 0
        width_2 = 100
        for i in check_list:
            height_1 = max(i[0],height_1)
            height_2 = min(i[2],height_2)
            width_1 = max(i[1],width_1)
            width_2 = min(i[3],width_2) 
        sum += (height_2-height_1) * (width_2-width_1)  
    
print(sum)    



