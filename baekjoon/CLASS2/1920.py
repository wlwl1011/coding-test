import sys

def binary_search(target, data):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = ( start + end ) // 2

        if data[mid] == target:
            return 1 #함수를 끝내버린다
        elif data[mid] < target:
            start = mid + 1
        else :
            end = mid - 1

    return None                            
    


n = int(sys.stdin.readline())
arr_n = list(map(int, sys.stdin.readline().split()))

#이분 탐색을 위한 정렬
arr_n.sort()

m = int(sys.stdin.readline())
arr_m = list(map(int, sys.stdin.readline().split()))

s = ""

for i, ele in enumerate(arr_m):

    idx = binary_search(ele, arr_n)

    if i < m-1:
        if idx :
            s +=str(1) + '\n'
        else:
            s +=str(0) + '\n'
    else : 
        if idx :
            s +=str(1)
        else:
            s +=str(0)   

print(s)