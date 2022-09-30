a, m, d, n = input().split()
a = int(a)
m = int(m)
d = int(d)
n = int(n)
sol = a
for i in range(1,n+1):
    
    if i == n:
        print(sol)

    sol = sol*m + d    

        