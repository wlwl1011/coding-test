a , b = input().split()
a = int(a)
b = int(b)

check_w = 1000
temp_w = 0

check_b = 1000
temp_b = 0

arr = [input() for _ in range(a)]


check_arr_w = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
check_arr_b = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB','BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']


for j in range(b//8 + 1):
    temp_w = 0
    for i in range(8):
        for k in range(8):
            if arr[i][k] != check_arr_w[i][k+j]:
                temp_w += 1 
            if arr[i][k] != check_arr_b[i][k+j]:  
                temp_b += 1   
    if check_w > temp_w:
        check_w = temp_w
    if check_b > temp_b:
        check_b = temp_b         

for j in range(a//8 + 1):
    temp_w = 0
    for i in range(8):
        for k in range(8):
            if arr[i][k] != check_arr_w[i+j][k]:
                temp_w += 1 
            if arr[i][k] != check_arr_b[i+j][k]:
                temp_b += 1 
    if check_b > temp_b:
        check_b = temp_b    
    if check_w > temp_w:
        check_w = temp_w     

if check_w > check_b :
    print(check_b)
else :
    print(check_w)
