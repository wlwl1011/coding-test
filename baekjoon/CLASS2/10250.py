import math

t = input()
t = int(t)


for i in range(t):
    h, w, n = map(int, input().split())
    roomHeight = n%h
    roomNumber = (math.ceil(n/h))%w
    if roomHeight == 0 :
        roomHeight = h
    if roomNumber == 0:
        roomNumber = w   
    roomHeight = roomHeight * 100
    room = roomHeight + roomNumber
    print(room)





