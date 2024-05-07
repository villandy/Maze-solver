from graphics import *
import random

class Cell:
    def __init__(self,win = None, seed = None):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        # for random seed generation
        self._seed = seed
        #keeps track of cells that had their walls broken
        self._visited = False
        if self._seed is not None:
            random.seed(seed)


    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1,y1), Point(x1,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y1), Point(x1,y2))
            self._win.draw_line(line,"white")            
        if self.has_right_wall:
            line = Line(Point(x2,y1), Point(x2,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2,y1), Point(x2,y2))
            self._win.draw_line(line,"white")
        if self.has_top_wall:
            line = Line(Point(x1,y2), Point(x2,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y2), Point(x2,y2))
            self._win.draw_line(line,"white")
        if self.has_bottom_wall:
            line = Line(Point(x1,y1), Point(x2,y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y1), Point(x2,y1))
            self._win.draw_line(line,"white")

    # draws a path between two cells
    # when undo is True, draw color should be gray, o.w red
    # First find centers of each cell
    def draw_move(self, to_cell, undo=False):
        half_legnth1 = abs(self._x2 - self._x1) // 2
        x_center = half_legnth1 + self._x1
        y_center = half_legnth1 + self._y1

        half_legnth2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_legnth2 + to_cell._x1
        y_center2 = half_legnth2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center,y_center), Point(x_center2,y_center2))
        self._win.draw_line(line, fill_color)

    # depth first traversal through cells, breaking walls as it goes
    # keeping track of which cells were traversed of course
    def _break_walls_r(self, i , j):
        self._cells[i][j]._visited = True
        while True:
            to_visit = []
            

