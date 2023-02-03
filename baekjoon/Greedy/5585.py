import sys

won = int(sys.stdin.readline())

won = 1000-won
check = 0

if won >= 500:
    check = check + won//500
    won = won % 500
if won >= 100:
    check = check + won//100
    won = won % 100
if won >= 50:
    check = check + won//50
    won = won % 50    
if won >= 10:
    check = check + won//10
    won = won % 10    
if won >= 5:
    check = check + won//5
    won = won % 5

check = check + won     
    
print(check)
    