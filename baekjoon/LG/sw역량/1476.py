import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())

e, s, m = 0, 0, 0
years = 0
while True:
    e = (e + 1) % 16
    s = (s + 1) % 29
    m = (m + 1) % 20

    if e == 0:
        e = 1
    if s == 0:
        s = 1
    if m == 0:
        m = 1
    years += 1
    if e == E and s == S and m == M:
        break

print(years)
