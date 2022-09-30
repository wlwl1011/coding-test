h, w = input().split()
h = int(h)
w = int(w)

arr = []
for i in range(h+1):
    arr.append([])
    for j in range(w+1):
        arr[i].append(0)

n = input()
n = int(n)

for i in range(n):
    l, d, x, y = input().split()
    l = int(l)
    d = int(d)
    x = int(x)
    y = int(y)
    if d==0:
        for i in range(l):
            arr[x][y+i]=1
    elif d==1:
        for i in range(l):
            arr[x+i][y]=1        
        
for i in range(1,h+1):
    for j in range(1,w+1):
        print(arr[i][j],end=" ")
    print()           


