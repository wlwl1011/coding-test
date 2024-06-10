import sys
input = sys.stdin.readline

def calculate_full_houses(n):
    N = 52 - n

    if N <= 26:
        min_cnt = 0
    else:
        if 27 <= N <= 29:
            min_cnt = 1
        elif N == 30:
            min_cnt = 2
        elif 31 <= N <= 33:
            min_cnt = 3
        elif N == 34:
            min_cnt = 4
        elif 35 <= N <= 37:
            min_cnt = 5
        elif N == 38:
            min_cnt = 6
        elif 39 <= N <= 41:
            min_cnt = 7
        else:
            min_cnt = 8

    max_cnt = min(8, N // 5)

    print(min_cnt, max_cnt)

# 입력: 밥이 가져간 카드의 수
n = int(input().strip())

# 결과 계산 및 출력
calculate_full_houses(n)
