import sys, os, io, atexit
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

total = 0
for i in range(5):
    first, second = input().split()
    first_h, first_m = map(int,first.split(':'))
    total_first = first_h * 60 + first_m
    second_h, second_m = map(int,second.split(':'))
    total_second = second_h * 60 + second_m
    total += total_second - total_first

print(total)
    