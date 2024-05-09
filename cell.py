from graphics import *

class Cell:
    def __init__(self,win = None):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
       


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

                

            

