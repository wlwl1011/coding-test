import sys

n = sys.stdin.readline().strip()
n = int(n)
arr= []

for i in range(n):
    temp = sys.stdin.readline().strip()
    temp = int(temp)
    arr.append(temp)

a = sorted(arr)

for i in range(n):
    print(a[i])