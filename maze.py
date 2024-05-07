from graphics import *
from cell import *
import time

class Maze:
    # holds all the cells in the maze in a 2-D grid
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        

        self._create_cells()
        

    # fills a list with lists of cells.
    # calls _draw_cell()
    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                cell = Cell(self._win)
                column.append(cell)
            self._cells.append(column)
            
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)
    # i = col, j = row 
    def _draw_cell(self,i,j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1,y1,x2,y2)
        self._animate()


    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols - 1][self._num_rows -1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

