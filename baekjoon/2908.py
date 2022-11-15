a, b = map(int, input().split())

tempA = 0
tempB = 0
div = 10
mux = 100

for i in range(1,3+1):
    
    tempA = tempA + (a % div) * mux
    tempB = tempB + (b % div) * mux

    a = a//10
    b = b//10
    mux = mux //10

if(tempA > tempB):
    print(tempA)
else:
    print(tempB)    