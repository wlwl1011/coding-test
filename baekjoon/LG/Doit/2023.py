import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import math

N = int(input())
answer = []
def isPrime(n):
    if n ==1:
        return True
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

    

def dfs(n):
    
    if n == 0:
        return
    # print(n)
    if len(str(n)) > N:
        return
    
    if isPrime(n):
        if len(str(n)) == N:
            if n not in answer:
                answer.append(n)
        
        else:
            for i in range(10):
                if i %2 ==0 :
                    continue
                new_n = str(n) + str(i)
                dfs(int(new_n))

for i in [2,3,5,7]:
    dfs(i)

for i in range(len(answer)):
    print(answer[i])