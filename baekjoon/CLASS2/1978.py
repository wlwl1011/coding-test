import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().strip().split()))


PrimeCheck = 0

for idx in arr:
    isPrime = True
    for i in range(2,idx):
        if idx % i == 0 :
            isPrime = False
    if isPrime:
  
        if idx != 1:
            PrimeCheck +=1   

print(PrimeCheck)