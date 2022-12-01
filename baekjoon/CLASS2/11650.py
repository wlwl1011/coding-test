import sys

n = int(sys.stdin.readline())
dic = {}


arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().strip().split())))


arr.sort()

for x, y in arr:
    print(x, y)