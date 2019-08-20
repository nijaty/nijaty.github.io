import math

class Point: 


    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, x1, y1):
        return math.sqrt(pow((x1-self.x),2) + pow((y1-self.y),2))

d = Point(3, 7)
print(d.calculate_distance(5,9))

        