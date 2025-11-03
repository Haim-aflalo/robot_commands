from classes.movable import MovableMixin
from classes.speakable import SpeakableMixin


class GuardRobot(SpeakableMixin):
    def __init__(self, name, say):
        super().__init__(name, say)

    def speak(self):
        print(f"{self.name}: '{self.say}'")

    def moving(self):
        print("i cant move")

    def where(self):
        print("i cant move")
