import sys
input = sys.stdin.readline


def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
cnt = 0
N, M = map(int, input().split())
parent = [i for i in range(N)]
check = []
truth = list(map(int, input().split()))

truth_people = truth[0]
if truth_people:
    truth = truth[1::]
    first = truth[0]
    for i in range(len(truth)):
        union(first-1,truth[i]-1)

for _ in range(M):
    people = list(map(int,input().split()))

    person = people[0]
    if person:
        people = people[1::]
        check.append(people)
        for i in range(len(people)):
            union(people[i]-1,people[0]-1)
cnt = 0
# print("first",first)
# print("---------")
# print(parent)
if truth_people:
    for c in check:
        flag = True
        # print("***")
        for i in range(len(c)):

            if find(c[i]-1) == find(first-1):
                flag = False
        if flag:
            cnt += 1
    print(cnt)
else:
    print(M)


