import time
def printDelay(t: str, d=1):
    time.sleep(d)
    print(t)

for i in range(30,-1,-1):
    printDelay(i) 
printDelay('de raketlancering is gestart!')