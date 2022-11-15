import time
def printDelay(t: str, d=1):
    time.sleep(d)
    print(t)

aftelling = 31
while aftelling >= 1:
    aftelling = aftelling - 1
    printDelay(aftelling)
printDelay('de raketlancering is gestart!')