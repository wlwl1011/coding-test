import math

x, y, w, h = input().split()

x = int(x)
y = int(y)
w = int(w)
h = int(h)

a = w - x
b = h - y

arr = []

arr.append(a)
arr.append(b)
arr.append(x)
arr.append(y)

arr.sort()

print(arr[0])