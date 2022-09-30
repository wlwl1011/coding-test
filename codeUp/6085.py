r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)

print(format(r*g*b/8/1024/1024,".2f") ,"MB")