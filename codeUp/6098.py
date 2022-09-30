d=[]
for i in range(12):
    d.append([])
    for j in range(12):
        d[i].append(1)

for i in range(1,11):
    temp = input().split()
    for j in range(1,11):
        temp[j-1] = int(temp[j-1])
        d[i][j] = (temp[j-1])    

x =2
y =2

while(1):
   

    if (d[x][y] == 2) or (d[x+1][y]==1 and d[x][y+1]==1) or (x==9 and y==9):
        d[x][y] = 9
        break
    
    d[x][y] = 9

    if d[x][y+1]%2 == 0 :
        y +=1
    else :
        x +=1    

for i in range(1,11):
    for j in range(1,11):
        print(d[i][j],end=" ")
    print()    
