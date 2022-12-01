import sys
class person(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return "'"+self.name+"'"



n = int(sys.stdin.readline())
dic = {}



for i in range(n):
    temp = sys.stdin.readline().strip().split()
    dic[person(temp[1])] = int(temp[0])
    

dic_sort = sorted(dic.items(), key=lambda x:x[1])

for key, value in dic_sort:
    print(value, key)