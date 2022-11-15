a = input().split()

sum = 0
for i in range(5):
    temp = int(a[i])
    sum = sum + temp*temp

print(sum%10)