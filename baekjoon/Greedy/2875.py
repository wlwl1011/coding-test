import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m, k = map(int,input().split())
answer = 0

n_num = n //2
m_num = m 

if n_num >= m_num:
    n -= k
    n_num = n //2
    answer = min(n_num,m_num)
else:
    m -= k
    m_num = m
    answer = min(n_num,m_num)    

print(answer)
