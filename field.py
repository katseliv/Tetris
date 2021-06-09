import random
import sys
import PyQt5.QtGui

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget

import logic
from game_over_window import GameOverWindow
from logic import mesh, create_forms, change_position, is_end


class Field(QWidget):
    WIDTH = 650
    HEIGHT = 750
    CELLS = logic.CELLS
    SIZE = logic.SIZE

    START_X = 120
    START_Y = 550
    START_X1 = 320
    START_X2 = 510

    form = create_forms(START_X, START_Y)
    form1 = create_forms(START_X1, START_Y)
    form2 = create_forms(START_X2, START_Y)

    def __init__(self, parent):
        super(Field, self).__init__()
        self.setParent(parent)
        self.initialize_component()

    def initialize_component(self):
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.setWindowTitle("Tetris")
        self.update()
        self.show()

    sign = -1
    SHIFT_X = 145
    SHIFT_Y = 50
    current_form = None
    list_of_forms = []

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.sign = self.count_destination(event.x(), event.y())
            if self.sign == 0:
                self.current_form = self.form
                self.form = None
            elif self.sign == 1:
                self.current_form = self.form1
                self.form1 = None
            elif self.sign == 2:
                self.current_form = self.form2
                self.form2 = None
        self.update()

    def count_destination(self, current_x, current_y):
        dx = current_x - self.START_X
        dy = current_y - self.START_Y

        d0 = (dx ** 2 + dy ** 2) ** 0.5
        dx = current_x - self.START_X1
        d1 = (dx ** 2 + dy ** 2) ** 0.5
        dx = current_x - self.START_X2
        d2 = (dx ** 2 + dy ** 2) ** 0.5

        m = min(d0, d1, d2)

        if m < 80:
            if m == d0:
                return 0
            elif m == d1:
                return 1
            elif m == d2:
                return 2
        else:
            return -1

    def mouseMoveEvent(self, event):
        if self.current_form is not None:
            change_position(self.current_form, event.x(), event.y())
        self.update()

    def mouseReleaseEvent(self, event):
        if self.SHIFT_X < event.x() < self.SHIFT_X + self.CELLS * self.SIZE and self.SHIFT_Y < event.y() < self.SHIFT_Y + self.CELLS * self.SIZE:
            if self.current_form is not None and self.set_placement() == 1:
                self.shift_forms()
                self.list_of_forms.append(self.current_form)
                self.current_form = None
            else:
                self.return_forms_to_own_position()
        else:
            self.return_forms_to_own_position()

        self.zero_full_lines()

        if is_end(self.form) and is_end(self.form1) and is_end(self.form2):
            dialog = GameOverWindow(parent=self)
            if dialog.exec():
                pass

        self.update()

    def paintEvent(self, e):
        self.painter = QPainter()
        self.painter.begin(self)
        self.draw_field(self.painter)
        self.painter.end()

    def draw_field(self, painter):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        for i in range(0, self.CELLS):
            for j in range(0, self.CELLS):
                x0, y0 = i * self.SIZE + self.SHIFT_X, j * self.SIZE + self.SHIFT_Y
                painter.setPen(pen)
                painter.setBrush(QColor(255, 255, 255))
                painter.drawRect(x0, y0, self.SIZE, self.SIZE)

        if self.list_of_forms is not None:
            for form in self.list_of_forms:
                form.draw(painter)

        if self.current_form is not None:
            self.current_form.draw(painter)

        if self.form is not None:
            self.form.draw(painter)

        if self.form1 is not None:
            self.form1.draw(painter)

        if self.form2 is not None:
            self.form2.draw(painter)

    def shift_forms(self):
        if self.sign == 0:
            self.form = self.form1
            change_position(self.form, self.START_X, self.START_Y)
            self.form1 = self.form2
            change_position(self.form1, self.START_X1, self.START_Y)
            self.form2 = create_forms(self.START_X2, self.START_Y)
        if self.sign == 1:
            self.form1 = self.form2
            change_position(self.form1, self.START_X1, self.START_Y)
            self.form2 = create_forms(self.START_X2, self.START_Y)
        if self.sign == 2:
            self.form2 = create_forms(self.START_X2, self.START_Y)

    def return_forms_to_own_position(self):
        if self.sign == 0:
            change_position(self.current_form, self.START_X, self.START_Y)
            self.form = self.current_form
        if self.sign == 1:
            change_position(self.current_form, self.START_X1, self.START_Y)
            self.form1 = self.current_form
        if self.sign == 2:
            change_position(self.current_form, self.START_X2, self.START_Y)
            self.form2 = self.current_form
        self.current_form = None

    def set_placement(self):
        column_ax = self.which_column(self.current_form.a.x + self.SIZE / 2)
        row_ay = self.which_row(self.current_form.a.y + self.SIZE / 2)
        column_bx = self.which_column(self.current_form.b.x + self.SIZE / 2)
        row_by = self.which_row(self.current_form.b.y + self.SIZE / 2)
        column_cx = self.which_column(self.current_form.c.x + self.SIZE / 2)
        row_cy = self.which_row(self.current_form.c.y + self.SIZE / 2)
        column_dx = self.which_column(self.current_form.d.x + self.SIZE / 2)
        row_dy = self.which_row(self.current_form.d.y + self.SIZE / 2)

        if column_ax == -1 or row_ay == -1 or column_bx == -1 or row_by == -1 or column_cx == -1 or row_cy == \
                -1 or column_dx == -1 or row_dy == -1:
            return -1

        if logic.can_form_be_located_here(column_ax, row_ay, column_bx, row_by, column_cx, row_cy, column_dx, row_dy):
            self.current_form.a.set_x(column_ax * self.SIZE + self.SHIFT_X)
            self.current_form.a.set_y(row_ay * self.SIZE + self.SHIFT_Y)
            mesh[row_ay][column_ax] = 1
            self.current_form.b.set_x(column_bx * self.SIZE + self.SHIFT_X)
            self.current_form.b.set_y(row_by * self.SIZE + self.SHIFT_Y)
            mesh[row_by][column_bx] = 1
            self.current_form.c.set_x(column_cx * self.SIZE + self.SHIFT_X)
            self.current_form.c.set_y(row_cy * self.SIZE + self.SHIFT_Y)
            mesh[row_cy][column_cx] = 1
            self.current_form.d.set_x(column_dx * self.SIZE + self.SHIFT_X)
            self.current_form.d.set_y(row_dy * self.SIZE + self.SHIFT_Y)
            mesh[row_dy][column_dx] = 1
            return 1
        else:
            return -1

    def which_column(self, current_x) -> int:
        for i in range(0, self.CELLS):
            x0 = i * self.SIZE + self.SHIFT_X
            if x0 < current_x <= x0 + self.SIZE:
                return i
        return -1

    def which_row(self, current_y) -> int:
        for j in range(0, self.CELLS):
            y0 = j * self.SIZE + self.SHIFT_Y
            if y0 < current_y <= y0 + self.SIZE:
                return j
        return -1

    def zero_full_lines(self):
        list_of_column_index = logic.check_full_column()
        list_of_row_index = logic.check_full_row()
        logic.zero_column(list_of_column_index)
        logic.zero_row(list_of_row_index)

        for index_column in list_of_column_index:
            self.zero_forms_by_x(index_column)

        for index_row in list_of_row_index:
            self.zero_forms_by_y(index_row)

    def zero_forms_by_x(self, index):
        x = index * self.SIZE + self.SHIFT_X
        for form in self.list_of_forms:
            if form.a is not None and form.a.x == x:
                form.set_a(None)
            if form.b is not None and form.b.x == x:
                form.set_b(None)
            if form.c is not None and form.c.x == x:
                form.set_c(None)
            if form.d is not None and form.d.x == x:
                form.set_d(None)

    def zero_forms_by_y(self, index):
        y = index * self.SIZE + self.SHIFT_Y
        for form in self.list_of_forms:
            if form.a is not None and form.a.y == y:
                form.set_a(None)
            if form.b is not None and form.b.y == y:
                form.set_b(None)
            if form.c is not None and form.c.y == y:
                form.set_c(None)
            if form.d is not None and form.d.y == y:
                form.set_d(None)
