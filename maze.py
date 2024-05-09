
from cell import Cell
import time
import random

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
            seed = None
            
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        #for random seed generation
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_dfs_r(0,0)
        self._reset_cells_visited()
        

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

    # depth first traversal through cells, breaking walls as it goes
    # keeping track of which cells were traversed of course
    def _break_walls_dfs_r(self, i , j):
        self._cells[i][j].visited = True
        while True:
            index_to_visit = []
            # determining adjacent LEFT cell
            if i > 0 and not self._cells[i-1][j].visited:
                index_to_visit.append((i - 1, j))
            
            # determining adjacent right cell
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                index_to_visit.append((i + 1, j))

            # determining adjacent top cell
            if j > 0 and not self._cells[i][j-1].visited:
                index_to_visit.append((i, j - 1))
            
            #determing adjacent bottom cell
            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                index_to_visit.append((i , j + 1))

            # if nowhere to go, draw the cell and break out
            if len(index_to_visit) == 0:
                self._draw_cell(i,j)
                return
            
            # otherwise pick a random direction
            # uses randrange 
            rand_dirction_index = random.randrange(len(index_to_visit))
            next_index = index_to_visit[rand_dirction_index]

            # knock walls of current direction: left
            # wall breaking works both ways ie. cell || curr_cell
            # if current row cell to the left
            if next_index[0] == i - 1:
                self._cells[i - 1][j].has_right_wall = False
                self._cells[i][j].has_left_wall = False

            # knock walls of current direction: right
            # if current row cell to the right 
            if next_index[0] == i + 1:
                self._cells[i + 1][j].has_left_wall = False
                self._cells[i][j].has_right_wall = False          

            #knock walls of current direction: up
            if next_index[1] == j - 1:
                self._cells[i][j - 1].has_top_wall = False
                self._cells[i][j].has_top_wall = False

            #knock walls of current direction: down
            if next_index[1] == j + 1:
                self._cells[i][j + 1].has_bottom_wall = False
                self._cells[i][j].has_bottom_wall = False
            
            # recursively move to chosen cell
            # where next[0] is the row position
            # next[1] is  is the column position
            self._break_walls_dfs_r(next_index[0], next_index[1])

    # resets all the cells in the Maze to False
    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False
    

    # dfs solution to the maze
    # returns True is current cell is an end cell or 
    # leads to the end of the cell
    # returns False if current cell is a "loser cell" ie. 
    # none of the directions worked out
    def _solve_dfs_r(self, i, j):
        self._animate()

        # current cell is visited
        self._cells[i][j].visited = True

        # reached "goal" ie. end cell
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            print("Winner Winner Chicken Dinner")
            return True  
        
        # look for goal for each direction
        # move left
        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i - 1][j].visited
        ):
            # draw a move between current cell to_cell
            # recall undo is a default parameter set to False
            self._cells[i][j].draw_move(self._cells[i-1][j])

            #recursively call this method to move to the cell
            # if true dont worry about other directions. else draw an undo move
            if self._solve_dfs_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)
        # move right
        if(
            i < self._num_cols -1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_dfs_r(i + 1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        #move up
        if(
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_dfs_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        
        # move down
        if(
            j < self._num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_dfs_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        # none of the directions worked out
        # so let previous cell know we took wrong direction
        return False
            
    # calls our dfs solution starting at 0,0
    def solve(self):
        self._solve_dfs_r(0,0)

        