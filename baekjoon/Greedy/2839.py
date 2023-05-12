import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))


n = int(input())
numbers = [5, 3]
answer = 0
leaves = [0]

while True:
    answer +=1
    temp = []
    for leaf in leaves:
        temp.append(leaf + numbers[0])
        temp.append(leaf + numbers[1])
        
    leaves = temp 

    if n in leaves:
        break
    elif n < min(leaves):
        answer = -1
        break
       

print(answer)