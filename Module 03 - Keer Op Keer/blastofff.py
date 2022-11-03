import time
def printDelay(t: str, d=0.5):
    time.sleep(d)
    print(t)

for i in range(30,0,-1):
    printDelay(i) 
printDelay('de raketlancering is gestart!')