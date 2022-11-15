from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')
robotArm.speed = 2

robotArm.grab()
for x in range(1,10):
    robotArm.moveRight()
robotArm.drop()
robotArm.moveLeft()
robotArm.moveLeft()
robotArm.grab()
for x in range(8,10):
    robotArm.moveRight()
robotArm.drop()
for x in range(1,6):
    robotArm.moveLeft()
robotArm.grab()
for x in range(6,11):
    robotArm.moveRight()
robotArm.drop()
robotArm.wait()