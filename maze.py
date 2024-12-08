import random
import time
from cell import Cell
from point import Point
from window import Window


class Maze:
    def __init__(
        self,
        p: Point,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window: Window,
        seed=None,
    ):
        self._p = p
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        if seed:
            random.seed(seed)
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for y in range(self._num_rows):
            cols = []
            for x in range(self._num_cols):
                cols.append(Cell(window=self._window))
            self._cells.append(cols)

    def draw(self):
        for y in range(self._num_rows):
            for x in range(self._num_cols):
                self._draw_cell(x, y)
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)

    def _draw_cell(self, x, y):
        p1 = Point(self._p.x + self._cell_size_x * x, self._p.y + self._cell_size_y * y)
        p2 = Point(
            self._p.x + self._cell_size_x * (x + 1),
            self._p.y + self._cell_size_y * (y + 1),
        )
        self._cells[x][y].p1 = p1
        self._cells[x][y].p2 = p2
        self._cells[x][y].draw()
        self._animate()

    def _animate(self):
        self._window.redraw()
        time.sleep(0.03)

    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_rows - 1][self._num_cols - 1].bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # left cell
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right cell
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # top cell
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # bottom cell
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # no where to go so breaak
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # choose a random direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # right direction wall removal
            if next_index[0] == i + 1:
                self._cells[i][j].right_wall = False
                self._cells[i + 1][j].left_wall = False
            # left direction wall removal
            if next_index[0] == i - 1:
                self._cells[i][j].left_wall = False
                self._cells[i - 1][j].right_wall = False
            # down direction wall removal
            if next_index[1] == j + 1:
                self._cells[i][j].bottom_wall = False
                self._cells[i][j + 1].top_wall = False
            # up direction wall removal
            if next_index[1] == j - 1:
                self._cells[i][j].top_wall = False
                self._cells[i][j - 1].bottom_wall = False

            # visit next cell
            self._break_walls_r(next_index[0], next_index[1])


