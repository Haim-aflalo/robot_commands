from classes.movable import MovableMixin
from classes.speakable import SpeakableMixin


class DeliveryRobot(SpeakableMixin, MovableMixin):

    def __init__(self, name, say,coordinates=0.0):
        super().__init__(name, say)
        self.coordinates= coordinates


    def speak(self):
        print(f"{self.name} : {self.say}")

    def moving(self,points):
            print(f"{self.name} moving on {points}")
            self.coordinates = points



    def where(self):
        if self.name == "Dora":
            print(f"{self.name} he's on the position {self.coordinates}")
        if self.name == "Gideon":
            print("unsupported command 'WHERE'")
