n = input()
n = int(n)

a = []
for i in range(n):
    a.append(0)

for i in range(n):
    a[i] = input()
    a[i] = int(a[i])

min = 10000
minIndex = 0
#sort
for i in range(n):
    min = 10000
    for j in range(i,n):
        if a[j]<min:
            min = a[j]
            minIndex = j

    temp = a[i]
    a[minIndex] = temp
    a[i] = min

for i in range(n):
    print(a[i])    


