n = int(input())

for i in range(0,n):
    r, s = input().split()
    r = int(r)
    for i in range(0, len(s)):
        print(s[i]*r,end='')
    print()    
