a, b = input().split()
a = int(a)
b = int(b)

if a > b :
    div = a
else :
    div = b


result = 1


for i in range(div,0,-1):
    if a%i == 0 and b%i == 0:
        a = a//i
        b = b//i
        
        result = result * i
        if a > b :
            div = a
        else :
            div = b

print(result)
print(result*a*b)



