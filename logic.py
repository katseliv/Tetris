import random
import numpy as np
from forms import Rectangle, Form

CELLS = 10
SIZE = 35
X_POSITION = 300
mesh = np.array([[0] * CELLS] * CELLS)


def create_forms(x_position, y_position):
    block = random.randint(0, 100)
    a = Rectangle(SIZE)
    b = Rectangle(SIZE)
    c = Rectangle(SIZE)
    d = Rectangle(SIZE)
    form = Form(a, b, c, d)

    if block < 15:
        j_block(form, x_position, y_position)
        name = "j"
    elif block < 30:
        l_block(form, x_position, y_position)
        name = "l"
    elif block < 45:
        o_block(form, x_position, y_position)
        name = "o"
    elif block < 60:
        s_block(form, x_position, y_position)
        name = "s"
    elif block < 75:
        t_block(form, x_position, y_position)
        name = "t"
    elif block < 90:
        z_block(form, x_position, y_position)
        name = "z"
    else:
        i_block(form, x_position, y_position)
        name = "i"

    form.set_name(name)
    return form


def change_position(form, x_position, y_position):
    name = form.name
    if name == 'j':
        j_block(form, x_position, y_position)
    elif name == 'l':
        l_block(form, x_position, y_position)
    elif name == 'o':
        o_block(form, x_position, y_position)
    elif name == 's':
        s_block(form, x_position, y_position)
    elif name == 't':
        t_block(form, x_position, y_position)
    elif name == 'z':
        z_block(form, x_position, y_position)
    elif name == 'i':
        i_block(form, x_position, y_position)


def j_block(form, x_position, y_position):
    form.a.set_x(x_position - SIZE)
    form.a.set_y(y_position)
    form.b.set_x(x_position - SIZE)
    form.b.set_y(y_position + SIZE)
    form.c.set_x(x_position)
    form.c.set_y(y_position + SIZE)
    form.d.set_x(x_position + SIZE)
    form.d.set_y(y_position + SIZE)


def l_block(form, x_position, y_position):
    form.a.set_x(x_position + SIZE)
    form.a.set_y(y_position)
    form.b.set_x(x_position - SIZE)
    form.b.set_y(y_position + SIZE)
    form.c.set_x(x_position)
    form.c.set_y(y_position + SIZE)
    form.d.set_x(x_position + SIZE)
    form.d.set_y(y_position + SIZE)


def o_block(form, x_position, y_position):
    form.a.set_x(x_position - SIZE)
    form.a.set_y(y_position)
    form.b.set_x(x_position)
    form.b.set_y(y_position)
    form.c.set_x(x_position - SIZE)
    form.c.set_y(y_position + SIZE)
    form.d.set_x(x_position)
    form.d.set_y(y_position + SIZE)


def s_block(form, x_position, y_position):
    form.a.set_x(x_position + SIZE)
    form.a.set_y(y_position)
    form.b.set_x(x_position)
    form.b.set_y(y_position)
    form.c.set_x(x_position)
    form.c.set_y(y_position + SIZE)
    form.d.set_x(x_position - SIZE)
    form.d.set_y(y_position + SIZE)


def t_block(form, x_position, y_position):
    form.a.set_x(x_position - SIZE)
    form.a.set_y(y_position)
    form.b.set_x(x_position)
    form.b.set_y(y_position)
    form.c.set_x(x_position)
    form.c.set_y(y_position + SIZE)
    form.d.set_x(x_position + SIZE)
    form.d.set_y(y_position)


def z_block(form, x_position, y_position):
    form.a.set_x(x_position)
    form.a.set_y(y_position)
    form.b.set_x(x_position - SIZE)
    form.b.set_y(y_position)
    form.c.set_x(x_position)
    form.c.set_y(y_position + SIZE)
    form.d.set_x(x_position + SIZE)
    form.d.set_y(y_position + SIZE)


def i_block(form, x_position, y_position):
    form.a.set_x(x_position - 2 * SIZE)
    form.a.set_y(y_position)
    form.b.set_x(x_position - SIZE)
    form.b.set_y(y_position)
    form.c.set_x(x_position)
    form.c.set_y(y_position)
    form.d.set_x(x_position + SIZE)
    form.d.set_y(y_position)


def can_form_be_located_here(c1, r1, c2, r2, c3, r3, c4, r4) -> bool:
    global mesh
    if mesh[r1][c1] == 0 and mesh[r2][c2] == 0 and mesh[r3][c3] == 0 and mesh[r4][c4] == 0:
        return True
    return False


def check_full_column():
    global mesh, CELLS
    list_of_index = []
    s = np.sum(mesh, axis=0)
    for i in range(0, len(s)):
        if s[i] == CELLS:
            list_of_index.append(i)

    if list_of_index is not None:
        return list_of_index
    return -1


def check_full_row():
    global mesh, CELLS
    list_of_index = []
    s = np.sum(mesh, axis=1)
    for i in range(0, len(s)):
        if s[i] == CELLS:
            list_of_index.append(i)

    if list_of_index is not None:
        return list_of_index
    return -1


def zero_column(list_of_column_index):
    global mesh
    if list_of_column_index != -1:
        for i in range(0, CELLS):
            for index_column in list_of_column_index:
                mesh[i][index_column] = 0


def zero_row(list_of_row_index):
    global mesh, CELLS
    if list_of_row_index != -1:
        for i in range(0, CELLS):
            for index_row in list_of_row_index:
                mesh[index_row][i] = 0


def is_end(form):
    name = form.name

    if name == 'j':
        for i in range(CELLS - 1):
            for j in range(CELLS - 2):
                if mesh[i][j] == 0 and mesh[i + 1][j] == 0 and mesh[i + 1][j + 1] == 0 and mesh[i + 1][j + 2] == 0:
                    return False
    elif name == 'l':
        for i in range(CELLS - 1):
            for j in range(CELLS - 2):
                if mesh[i + 1][j] == 0 and mesh[i + 1][j + 1] == 0 and mesh[i + 1][j + 2] == 0 and mesh[i][j + 2] == 0:
                    return False
    elif name == 'o':
        for i in range(CELLS - 1):
            for j in range(CELLS - 1):
                if mesh[i][j] == 0 and mesh[i + 1][j] == 0 and mesh[i][j + 1] == 0 and mesh[i + 1][j + 1] == 0:
                    return False
    elif name == 's':
        for i in range(CELLS - 1):
            for j in range(CELLS - 2):
                if mesh[i + 1][j] == 0 and mesh[i + 1][j + 1] == 0 and mesh[i][j + 1] == 0 and mesh[i][j + 2] == 0:
                    return False
    elif name == 't':
        for i in range(CELLS - 1):
            for j in range(CELLS - 2):
                if mesh[i][j] == 0 and mesh[i][j + 1] == 0 and mesh[i + 1][j + 1] == 0 and mesh[i][j + 2] == 0:
                    return False
    elif name == 'z':
        for i in range(CELLS - 1):
            for j in range(CELLS - 2):
                if mesh[i][j] == 0 and mesh[i][j + 1] == 0 and mesh[i + 1][j + 1] == 0 and mesh[i + 1][j + 2] == 0:
                    return False
    elif name == 'i':
        for i in range(CELLS):
            for j in range(CELLS - 3):
                if mesh[i][j] == 0 and mesh[i][j + 1] == 0 and mesh[i][j + 2] == 0 and mesh[i][j + 3] == 0:
                    return False

    return True
