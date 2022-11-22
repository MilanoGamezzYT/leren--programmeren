from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
r = 9
l = 8
robotArm.speed=2
for i in range(5):
    robotArm.grab()
    for i in range(r):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(l):
        robotArm.moveLeft()
    r = r - 2
    l = l - 2


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()