from graphics import *
from cell import *
from maze import *
def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800 # window width
    screen_y = 600 #window height
    #takes total usable width and divides by num of columns
    cell_size_x = (screen_x - 2 * margin ) / num_cols
    #same calcultion as above but with height and num rows
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x,screen_y)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze._break_entrance_and_exit()
    win.wait_for_close()
main()