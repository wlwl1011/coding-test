n = input()
n = int(n)


for i in range(0,n):
    acc =1
    sum = 0
    str = input()
    for j in range(0,len(str)-1):
        if(str[j]=='O'):
            sum = sum + acc
            if(str[j] == str[j+1]):
                acc = acc+1
        else :
            acc=1 
    if(str[len(str)-1]=='O'):
       sum = sum + acc                
    print(sum)
