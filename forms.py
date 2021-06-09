from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen


class Form:
    a = property(lambda self: self.__a)
    b = property(lambda self: self.__b)
    c = property(lambda self: self.__c)
    d = property(lambda self: self.__d)

    def __init__(self, a, b, c, d, name=None):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.name = name
        self.set_color(name)

    def set_a(self, a):
        self.__a = a

    def set_b(self, b):
        self.__b = b

    def set_c(self, c):
        self.__c = c

    def set_d(self, d):
        self.__d = d

    def set_name(self, name):
        self.name = name
        self.set_color(name)

    def set_color(self, name):
        if name == 'j':
            self.color = QColor(89, 102, 127)
        elif name == 'l':
            self.color = QColor(147, 106, 44)
        elif name == 'o':
            self.color = QColor(151, 87, 85)
        elif name == 's':
            self.color = QColor(22, 134, 44)
        elif name == 't':
            self.color = QColor(84, 138, 153)
        elif name == 'z':
            self.color = QColor(207, 124, 182)
        elif name == 'i':
            self.color = QColor(230, 164, 87)

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        self.draw(painter)
        painter.end()

    def draw(self, painter):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.setBrush(self.color)
        if self.__a is not None:
            painter.drawRect(self.__a.x, self.__a.y, self.__a.width, self.__a.width)
        if self.__b is not None:
            painter.drawRect(self.__b.x, self.__b.y, self.__b.width, self.__b.width)
        if self.__c is not None:
            painter.drawRect(self.__c.x, self.__c.y, self.__c.width, self.__c.width)
        if self.__d is not None:
            painter.drawRect(self.__d.x, self.__d.y, self.__d.width, self.__d.width)


class Rectangle:
    x = property(lambda self: self.__x)
    y = property(lambda self: self.__y)

    def __init__(self, width, height=None, x=0, y=0):
        self.__x = x
        self.__y = y
        self.width = width
        self.height = height

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y
