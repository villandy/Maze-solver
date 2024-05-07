from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Boot.dev Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height,width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    # will redraw all the graphics in the window
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color="red"):
        line.draw(self.__canvas, fill_color)

    #change state of is_running
    def wait_for_close(self):
        self.__is_running = True
        
        while self.__is_running:
            self.redraw()
        print("Closing Window")

    # set is_running to false
    def close(self):
        self.__is_running = False

            
class Point:
    def __init__(self, x, y,):
        self.x = x
        self.y = y

    
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self,canvas,fill_color="red"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )



    
