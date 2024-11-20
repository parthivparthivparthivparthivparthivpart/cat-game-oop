import numpy as np
class shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def CalcArea(self):
        int(self.length) * int(self.width)

class circle(shape):
    def __init__(self, length):
        super().__init__(length)

    def CalcArea(self):
        ((int(self.length) / 2 )**2) * 3.14
    def perimeter(self):
        int(self.length) * 3.14

class rectangle(shape):
    def __init__(self, length, width):
        super().__init__(length, width)
    def CalcArea(self):
        super().CalcArea(self)
    def perimeter(self):
        int(self.length) + int(self.length) + int(self.width) + int(self.width)

class triangle(shape):
    def __init__(self, length, height):
        super().__init__(length)
        self.height = height
    def CalcArea(self):
        (int(self.length) * int(self.height)) / 2
class Right_angle_T(triangle):
    def __init__(self, length, height, angle):
        super().__init__(length, height)
        self.angle = angle
    def FINDHYP(self):
         self.height / (np.sin(int(self.angle)))
    def perimeter(self):
        hyp = self.FINDHYP()
        int(self.length) + int(self.height) + hyp

Tri = Right_angle_T("3", "4", "36.87")
Tri.FINDHYP()

