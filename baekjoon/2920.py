a = input().split()


for i in range (0, len(a)):
    a[i]=int(a[i])

if(sorted(a)==a):
    print('ascending')
elif(sorted(a, reverse=True)==a):
    print('descending')
else:
    print('mixed')        

        
