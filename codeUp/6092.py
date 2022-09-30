n = input()
n = int(n)

a = input().split()

for i in range(0,n):
    a[i] = int(a[i])

d = []
for i in range(24):
    d.append(0)

for i in range(n):
    d[a[i]] += 1

for i in range(1,24):
    print(d[i],end=" ")    

