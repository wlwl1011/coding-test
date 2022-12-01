
arr = []

for i in range(10):
    temp = input()
    temp = int(temp)
    temp = temp%42
    arr.append(temp)


arr.sort()
count = 0
for i in range(0,9):
    if arr[i] != arr[i+1]:
        count = count + 1

print(count+1)        