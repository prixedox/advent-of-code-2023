import numpy as np

class Expander:

    def __init__(self, grid):
        self.grid = grid

    def expand(self):
        rows, cols = self.get_empty_lines()

        self.grid = np.insert(self.grid, rows, self.grid[rows[0]], axis=0)
        self.grid = np.insert(self.grid.T, cols, self.grid.T[cols[0]], axis=0).T

        return self.grid

    def get_empty_lines(self):
        rows = []
        cols = []

        for i in range(self.grid.shape[0]):
            if (self.grid[i] == ".").all():
                rows.append(i)

        for j in range(self.grid.T.shape[0]):
            if (self.grid.T[j] == ".").all():
                cols.append(j)
        
        return np.array(rows), np.array(cols)