# Мельчук А.Б.
import math
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_vector_size(point1, point2):
    return ((point2.x - point1.x) * (point2.x - point1.x) + (point2.y - point1.y) * (point2.y - point1.y)) ** .5


class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

        self.side_a = get_vector_size(point1, point2)
        self.side_b = get_vector_size(point2, point3)
        self.side_c = get_vector_size(point3, point1)

    def __str__(self):
        return '[({},{}),({},{}),({},{})]'.format(self.point1.x, self.point1.y,
                                                  self.point2.x, self.point2.y,
                                                  self.point3.x, self.point3.y)

    @property
    def sides(self):
        return self.side_a, self.side_b, self.side_c

    def perimeter(self):
        return sum(self.sides)

    @property
    def p(self):  # half perimeter
        return self.perimeter() / 2

    def h_side(self, side):
        return 2 * self.square() / side

    @property
    def heights(self):
        return self.h_side(self.side_a), self.h_side(self.side_b), self.h_side(self.side_c)

    def square(self):
        return (self.p * (self.p - self.side_a) * (self.p - self.side_b) *
                (self.p - self.side_c)) ** .5

    def info(self):
        print(self)
        print('Sides =', self.sides)
        print('Side-a =', self.side_a)
        print('Side-b =', self.side_b)
        print('Side-c =', self.side_c)
        print('Perimeter =', self.perimeter())
        print('p =', self.p)
        print('S =', self.square())
        print('Heights =', self.heights)


print('Task 1')
triangle = Triangle(Point(1, 1), Point(40, 40), Point(60, 3))
triangle.info()

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
print('\n\nTask 2')


class Barrel:
    def __init__(self, point1, point2, point3, point4):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4

        self.side_a = get_vector_size(point1, point2)
        self.side_b = get_vector_size(point2, point3)
        self.side_c = get_vector_size(point3, point4)
        self.side_d = get_vector_size(point4, point1)

    def __str__(self):
        return '[({},{}),({},{}),({},{}),({},{})]'.format(self.point1.x, self.point1.y,
                                                          self.point2.x, self.point2.y,
                                                          self.point3.x, self.point3.y,
                                                          self.point4.x, self.point4.y)

    @property
    def sides(self):
        return self.side_a, self.side_b, self.side_c, self.side_d

    @property
    def x(self):
        return self.point1.x, self.point2.x, self.point3.x, self.point4.x

    @property
    def y(self):
        return self.point1.y, self.point2.y, self.point3.y, self.point4.y

    def perimeter(self):
        return sum(self.sides)

    # S = 1/2 |(x1 y2 - x2 y1) + (x2 y3 - x3 y2) + .. + (xn y1 - x1 yn)| - Pick's theorem, polygon area
    def square(self):
        return (1 / 2) * abs((self.x[0] * self.y[1] - self.x[1] * self.y[0]) +
                             (self.x[1] * self.y[2] - self.x[2] * self.y[1]) +
                             (self.x[2] * self.y[3] - self.x[3] * self.y[2]) +
                             (self.x[3] * self.y[0] - self.x[0] * self.y[3]))

    def angle(self, anchor):
        dx1 = self.x[3 if anchor == 0 else anchor - 1] - self.x[anchor]
        dy1 = self.y[3 if anchor == 0 else anchor - 1] - self.y[anchor]
        dx2 = self.x[0 if anchor == 3 else anchor + 1] - self.x[anchor]
        dy2 = self.y[0 if anchor == 3 else anchor + 1] - self.y[anchor]
        return math.atan2(dx1 * dy2 - dy1 * dx2, dx1 * dx2 + dy1 * dy2)

    def is_isosceles(self):  # base angles
        return (self.angle(0) == self.angle(1) and self.angle(2) == self.angle(3)) or\
               (self.angle(0) == self.angle(3) and self.angle(1) == self.angle(2))


    def info(self):
        print(self)
        print('Sides =', self.sides)
        print('Perimeter =', self.perimeter())
        print('S =', self.square())
        print('Angle at anchor 0 =', self.angle(0))
        print('Angle at anchor 1 =', self.angle(1))
        print('Angle at anchor 2 =', self.angle(2))
        print('Angle at anchor 3 =', self.angle(3))
        print('Trapezium is', self.is_isosceles(), 'isosceles.\n')


barrel = Barrel(Point(1, 7), Point(8, 2), Point(8, 4), Point(1, 9))
barrel.info()

barrel2 = Barrel(Point(1, 1), Point(10, 1), Point(8, 6), Point(5, 6))
barrel2.info()

barrel3 = Barrel(Point(-7, 0), Point(-5, 8), Point(5, 8), Point(7, 0))
barrel3.info()
