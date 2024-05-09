from tkinter import Tk, BOTH, Canvas, Text

class Window:
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title("Boot.dev Maze Solver")
        self._canvas = Canvas(self._root, bg="white", height=height,width=width)
        self._canvas.pack(fill=BOTH, expand=1)
        self._is_running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

        # Adding some text
        self._canvas.create_text(150, 50, text = "Solve the Maze", fill="black", font=('Helvetica 36 bold'))
     
        

    # will redraw all the graphics in the window
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def draw_line(self, line, fill_color="black"):
        line.draw(self._canvas, fill_color)

    #change state of is_running
    def wait_for_close(self):
        self._is_running = True
        
        while self._is_running:
            self.redraw()
        print("Closing Window")

    # set is_running to false
    def close(self):
        self._is_running = False

            
class Point:
    def __init__(self, x, y,):
        self.x = x
        self.y = y

    
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self,canvas,fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )



    
