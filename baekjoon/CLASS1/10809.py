s = input()
abc = 'abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in s:
        print(s.index(i),end=' ') #s안에서 i가 있는 위치를 찾아서 반환한다.
    else:
        print(-1, end=' ')    
