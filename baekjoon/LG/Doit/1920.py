import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def isHere(n,start,end):
  
    if start <= end:
        mid = (start + end) // 2

        if n == arr[mid]:
            return True
        elif n < arr[mid]:
            return isHere(n,start,mid-1)
        else:
            return isHere(n,mid+1,end)
    else:
        return False



N = int(input())

arr = list(map(int, input().split()))
arr.sort()
M = int(input())
check = list(map(int, input().split()))

for c in check:
    if isHere(c,0,N-1):
        print(1)
    else:
        print(0)