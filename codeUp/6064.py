a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

temp = (a if(a<b) else b)
min = temp if(temp < c) else c
print(min)