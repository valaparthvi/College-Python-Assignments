from math import pi, pow


class Circle:
    def __init__(self):
        self.radius = float(input("Enter radius of the circle: "))

    def areaOfCircle(self):
        area = pi * pow(self.radius, 2)
        print("Area of the circle is %f" % area)

    def perimeterOfCircle(self):
        perimeter = 2 * pi * self.radius
        print("Perimeter of the circle is %f" % perimeter)


if __name__ == '__main__':
    c1 = Circle()
    c1.areaOfCircle()
    c1.perimeterOfCircle()

'''
Output: python3 chapter5_2_circle.py
Enter radius of the circle: 5
Area of the circle is 78.539816
Perimeter of the circle is 31.415927
'''
