
d=[]



for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

for i in range(1,20):
    temp = input().split()
    for j in range(1,20):
        temp[j-1] = int(temp[j-1])
        d[i][j]=temp[j-1]
        

n = input()
n = int(n)

for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)

    for i in range(1,20):

        if d[x][i]==1:
            d[x][i]=0
        else:
            d[x][i] = 1

        if d[i][y]==1:
            d[i][y]=0
        else:
            d[i][y] = 1    


        

     
    


for i in range(1,20):
    for j in range(1,20):
        print(d[i][j],end=" ")
    print()    
       
    
