arr = []

arr = list(map(int,input().split()))
arr.sort() 

while arr[0] != 0 and arr[1] != 0 and arr[2] !=0 :
    if arr[0]*arr[0] + arr[1]*arr[1] == arr[2]*arr[2] :
        print("right")
    else:
        print("wrong")  

    arr = list(map(int,input().split()))
    arr.sort()      
    
