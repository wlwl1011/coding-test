n = input()
n = int(n)
arr = []
max = 0
sum = 0

temp = input().split()

for i in range(n):
    arr.append(int(temp[i]))


for i in range(n):
    if(arr[i]>max):
        max = arr[i]

for i in range(n):
    sum = sum + arr[i]/max*100

print(format(sum/n,".2f"))

