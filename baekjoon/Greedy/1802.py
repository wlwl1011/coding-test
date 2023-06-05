import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))


t = int(input()) #테스트 케이스 갯수
arr = []
arr = list(map(int,input())) #1 아웃, 0 인

