from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
for x in range(9):
    robotArm.grab()
    if robotArm.scan() == "red":
        for x in range(1):
            robotArm.moveRight()
        robotArm.drop()
    else:
        robotArm.drop()
        robotArm.moveRight()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()