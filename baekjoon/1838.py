n = input()
n = int(n)

a = input().split()

for i in range(n):
    a[i] = int(a[i])

for i in range(n):
    flag = 0
    for j in range(n-1):
        if a[j] > a[j+1]:
            flag = 1
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
    if flag == 0 :
        index = i
        break  
                  
print(index)