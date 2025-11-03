from classes.robot import Robot
from abc import ABC,abstractmethod

class MovableMixin(Robot,ABC):

    @abstractmethod
    def moving(self):
       pass

