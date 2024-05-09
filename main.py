from graphics import *
from cell import *
from maze import *
def main():
    num_rows = 10
    num_cols = 12
    margin = 150
    screen_x = 1000 # window width
    screen_y = 1000 #window height
    #takes total usable width and divides by num of columns
    #cell_size_x = (screen_x - 2 * margin ) / num_cols
    #same calcultion as above but with height and num rows
    #cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x,screen_y)
    maze = Maze(margin, margin, num_rows, num_cols, 50, 50, win, 10)
    
    maze.solve()
   
    win.wait_for_close()
main()