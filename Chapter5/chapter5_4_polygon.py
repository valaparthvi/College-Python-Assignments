from math import sqrt


class Polygon:
    def __init__(self):
        self.number_of_sides = int(input("Enter total number of sides: "))
        self.side_list = list()

    def inputSides(self):
        self.side_list = [int(input()) for i in range(self.number_of_sides)]

    def dispSides(self):
        print("Sides are: %s" % self.side_list)


class Triangle(Polygon):
    def areaOfTriangle(self):
        self.s = sum(self.side_list) / 2
        product = self.s
        for side in self.side_list:
            product *= (self.s - side)
        self.area = sqrt(product)
        print("Area of the Triangle with sides %s is %f" %
              (self.side_list, self.area))


if __name__ == '__main__':
    tri1 = Triangle()
    print("Input the magnitude of sides:")
    tri1.inputSides()
    tri1.dispSides()
    tri1.areaOfTriangle()


'''
Output: python3 chapter5_4_polygon.py
Enter total number of sides: 3
Input the magnitude of sides:
3
4
5
Sides are: [3, 4, 5]
Area of the Triangle with sides [3, 4, 5] is 6.000000
'''
