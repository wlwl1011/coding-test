from math import factorial

a, b = input().split()
a = int(a)
b = int(b)

print(factorial(a)//(factorial(b)*factorial(a-b)))