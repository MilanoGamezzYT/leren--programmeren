from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 1
x = 1
for h in range(4):
    for h in range(x):
        robotArm.grab()
        for h in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for h in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()
    x += 1


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()