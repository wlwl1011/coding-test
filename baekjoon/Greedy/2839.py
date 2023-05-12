import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))


n = int(input())

answer = 0

while n>=0:
   if n % 5 == 0:
      answer += n//5
      print(answer)
      break
   n -= 3
   answer += 1
else:
   print(-1)

print(answer)