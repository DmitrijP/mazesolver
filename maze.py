
import time
from cell import Cell
from point import Point
from window import Window


class Maze:
    def __init__(self, p: Point, 
                 num_rows, num_cols, 
                 cell_size_x, cell_size_y, 
                 window: Window):
        self._p = p
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
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
                self._draw_cell(x,y)
        self._break_entrance_and_exit()
    
    def _draw_cell(self, x, y):
        p1 = Point(self._p.x + self._cell_size_x * x, 
                   self._p.y + self._cell_size_y * y)
        p2 = Point(self._p.x + self._cell_size_x * (x + 1), 
                   self._p.y + self._cell_size_y * (y + 1))
        self._cells[x][y].p1 = p1
        self._cells[x][y].p2 = p2
        self._cells[x][y].draw()
        self._animate()
    
    def _animate(self):
        self._window.redraw()
        time.sleep(0.03)
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_rows - 1][self._num_cols - 1].bottom_wall = False
        self._draw_cell(self._num_rows - 1,self._num_cols - 1)