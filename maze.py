
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
                p1 = Point(self._p.x + self._cell_size_x * x, self._p.y + self._cell_size_y * y)
                p2 = Point(self._p.x + self._cell_size_x * (x + 1), self._p.y + self._cell_size_y * (y + 1))
                c = Cell(window=self._window, p1=p1, p2=p2)
                cols.append(c)
                c.draw()
            self._cells.append(cols)
                
    
    def _draw_cell(self, i, j):
        pass
    
    def _animate(self):
        pass