import unittest
from maze import Maze
from cell import Cell

class Tests(unittest.TestCase):
    # testing for correct maze dimensions
    # recall m1._cells is just number of columns
    # m1._cells[0] is accessing those columns of which the rows are located 
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    # testing for correct maze dimensions of a larger maze
    # same logic as last test
    def test_maze_create_cells_larger(self):
        num_cols = 18
        num_rows = 12
        m1 = Maze(10, 10, num_rows, num_cols, 50, 50)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    # testing for correct maze dimension of a smaller maze
    def test_maze_create_cells_smaller(self):
        num_rows = 2
        num_cols = 4
        m1 = Maze(0, 0, num_rows, num_cols, 5, 5)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )
    # tests correctness of break_entrance_exit
    def test_maze_break_entrance_and_exit(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_maze_reset_cells(self):
        pass


    

if __name__ == "__main__":
    unittest.main()