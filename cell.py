from graphics import *

class Cell:
    def __init__(self,win):
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1,y1), Point(x1,y2))
            self.__win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2,y1), Point(x2,y2))
            self.__win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1,y2), Point(x2,y2))
            self.__win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1,y1), Point(x2,y1))
            self.__win.draw_line(line)

    # draws a path between two cells
    # when undo is True draw color should be gray, o.w red
    def draw_move(self, to_cell, undo=False):
        pass
