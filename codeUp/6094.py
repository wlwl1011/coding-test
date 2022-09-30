n = input()
n = int(n)

a = input().split()

for i in range(n):
    a[i] = int(a[i])

min = 1000
for i in range(n):
    if a[i]<min :
        min = a[i]

print(min)