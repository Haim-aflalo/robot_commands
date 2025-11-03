from classes.delivery import DeliveryRobot
from classes.guard import GuardRobot

robot1 = DeliveryRobot("Dora","hi")
robot2 = GuardRobot("Gideon","hello")

robot1.speak()
robot2.speak()
robot2.moving()
