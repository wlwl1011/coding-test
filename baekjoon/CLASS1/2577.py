a = input()
b = input()
c = input()

a= int(a)
b = int(b)
c = int(c)

arr = []

for i in range(10):
    arr.append(0)

mux = a*b*c
div = 10


while(1):
    temp = mux%div
    arr[temp] = arr[temp]+1
    mux = mux//div
    if(mux<=0):
        break

for i in range(10):
    print(arr[i])    