import sys
from collections import deque
input = sys.stdin.readline

def calculator(a,b,operator):
    if operator == '+':
        return a+b
    else:
        return a-b

s = input().rstrip()

operator = deque()
operand = deque()

temp =''
for a in s:
    if str(a).isdigit(): 
        temp += str(a)
        
    else:
        operator.append(a)
        operand.append(int(temp))
        temp = ''
operand.append(int(temp))
# print("operator:",operator)
# print("operand:",operand)
total_sum = 0

total_sum = operand.popleft()

while operator:
    
    op = operator.popleft()
    b = operand.popleft()
    # print(a,op,b)
    if op == '-':
        while operator and operator[0]!='-':
            c = operand.popleft()
            temp_op = operator.popleft()
            b = calculator(b,c,temp_op)
    total_sum = calculator(total_sum,b,op)

print(total_sum)

