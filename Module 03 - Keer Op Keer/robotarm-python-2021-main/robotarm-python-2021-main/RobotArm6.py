from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
robotArm.speed = 1

for x in range(3):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
robotArm.wait()
