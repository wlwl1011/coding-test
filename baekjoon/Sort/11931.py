import sys

n = int(sys.stdin.readline())

arr = [0] * n

for i in range(n):
    temp = int(sys.stdin.readline())
    arr[i] = temp 

arr.sort(reverse=True)
for i in arr:
    print(i)

