n = input()
n = int(n)

for i in range(1, n+1):
    for k in range(1, n+1):
        if(n-i+1 <= k):
            print('*',end="")
        else:    
            print(' ',end='')
    print()    