a = []
max = 0
maxIndex = 0

#초기화
for i in range(9):
    a.append(0)

for i in range(0,9):
    a[i] = int(input())
    if max<a[i]:
        max = a[i]
        maxIndex = i

print(max)
print(maxIndex+1)
    



