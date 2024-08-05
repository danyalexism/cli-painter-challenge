
import matplotlib.pyplot as plt
import pickle


class Point:
    def __init__(self, x, y):
        self.x = 0
        self.y = 0
pt1 = Point()
pt2 = Point()

class Circle:
pi = 3.1416

    def __init__(self, center, radius):
      self.center = center
      self.radius = radius
    def area (self):
        return pi * self.radius ^2
    def draw (self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()
    def _str_ (x,y):
        Circle with center at (x, y) and radius r

class Triangle:

