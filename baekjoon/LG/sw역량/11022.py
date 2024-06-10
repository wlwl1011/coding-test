import sys
input = sys.stdin.readline

#테스트 케이스를 입력 받는다.
T = int(input())

for idx in range(1,T+1):
    #A와 B를 입력 받는다.
    A, B = map(int, input().split())

    #양식에 맞게 출력한다
    print(f"Case #{idx}: {A} + {B} = {A+B}")