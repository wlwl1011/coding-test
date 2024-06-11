import sys

# 전체 입력을 읽어들입니다.
input = sys.stdin.read

# 입력받은 내용을 줄 단위로 분할합니다.
lines = input().splitlines()

# 각 줄을 그대로 출력합니다.
for line in lines:
    print(line)
