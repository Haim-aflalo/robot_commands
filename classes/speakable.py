from classes.robot import Robot
from abc import ABC,abstractmethod

class SpeakableMixin(Robot, ABC):

    @abstractmethod
    def speak(self):
        pass


