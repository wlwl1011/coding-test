import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

arr = [[] for _ in range(4)]

for i in range(4):
    arr[i] = list(map(int, input()))

k = int(input())



for i in range(k):
    num, rotate = map(int, input().split())

    #돌려야했던 대상돌리기 
    temp = 0
    #반시계 방향
    if rotate == 0:
        temp = arr[num-1][0]
        for i in range(8):
            if i == 7:
                arr[num-1][i] = temp
            else:    
                arr[num-1][i] = arr[num-1][i+1]
    #시계 방향            
    else:
        for i in range(8):
            if i == 0:
                temp = arr[num-1][i-1]
                arr[num-1][0] = arr[num-1][7]
            else:    
                check = arr[num-1][i]   
                arr[num-1][i] = temp
                temp = check


    #지금 돌린 애 옆에 있어서 저절로 돌아가는 애들 ..
    
#     if num-1 == 0 and arr[0][2] != arr[1][6]:
#         #시계 방향이었으면
#         if rotate == 1:
#             #반시계로
#             temp = arr[1][7]
#             for i in range(8):
#                 check = arr[1][i] 
#                 arr[1][i] = temp
#                 temp = check
                    
#         else:
#              #시계로
#             temp = arr[1][0]
#             for i in range(8):
#                 if i == 7:
#                     arr[1][i] = temp
#                 else:    
#                     arr[1][i] = arr[1][i+1]       

#     elif num-1 == 3 and arr[2][2] != arr[3][6]:
#         if rotate == 1:
#             #반시계로
#             temp = arr[2][7]
#             for i in range(8):
#                 check = arr[2][i] 
#                 arr[2][i] = temp
#                 temp = check
#         else:
#              #시계로
#             temp = arr[2][0]
#             for i in range(8):
#                 if i == 7:
#                      arr[2][i] = temp
#                 else:    
#                     arr[2][i] = arr[2][i+1]     

#     else:
        
#         if arr[num-2][2] != arr[num-1][6]:
#             if rotate == 1:
#             #반시계로
#                 temp = arr[num-2][7]
#                 for i in range(8):
#                     check = arr[num-2][i] 
#                     arr[num-2][i] = temp
#                     temp = check
#             else:
#              #시계로
#                 temp = arr[num-2][0]
#                 for i in range(8):
#                     if i == 7:
#                         arr[num-2][i] = temp
#                     else:    
#                         arr[num-2][i] = arr[num-2][i+1]  
                
#         if arr[num-1][2] != arr[num][6]:
#             if rotate == 1:
#             #반시계로
#                 temp = arr[num][7]
#                 for i in range(8):
#                     check = arr[num][i] 
#                     arr[num][i] = temp
#                     temp = check
#             else:
#              #시계로
#                 temp = arr[num][0]
#                 for i in range(8):
#                     if i == 7:
#                         arr[num][i] = temp
#                     else:    
#                         arr[num][i] = arr[num][i+1]  

for i in range(4):
    print(arr[i])

# sum = 0
# if arr[0][0] == 1:
#     sum += 1
# if arr[1][0] == 1:
#     sum += 2
# if arr[2][0] == 1:
#     sum += 4
# if arr[3][0] == 1:
#     sum += 8

# print(sum)

   