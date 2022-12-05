
number = input()

s = ""

while number !="0" :
   
    flag = True
    idx = 0
    start = 0 
    end = len(number)-1
    while start<end:
        start += (idx)
        end -= (idx)
        if start>=end:
            break
        if  number[start] != number[end] :
            flag = False    
        idx +=1
         
    if flag == True:
        print("yes")
    else:
        print("no")

    number = input()

    if int(number) == 0:
        break
    