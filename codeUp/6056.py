a, b = input().split()
a = int(a)
b = int(b)

print((bool(a) and not bool(b)) or (bool(b) and not bool(a)))