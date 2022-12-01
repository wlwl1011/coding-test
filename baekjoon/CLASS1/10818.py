n = input()
n = int(n)

a = input().split()

for i in range(n):
    a[i] = int(a[i])

a.sort()

print(a[0],a[n-1])




