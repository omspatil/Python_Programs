"""Create a class Circle. Calculate the area of the cicle and show the area of cicle"""


class circle:
    def __init__(self, r) -> None:
        self.radius = r
        self.area = 0

    def calculateArea(self):
        self.area = 3.14*self.radius*self.radius
        print("Area is", self.area)


ob1 = circle(1.2)
ob2 = circle(3.4)
ob1.calculateArea()
ob2.calculateArea()
