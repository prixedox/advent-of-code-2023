import numpy as np
from heapq import heappush, heappop

class Traverser:

    def __init__(self, grid):
        self.grid = grid
        self.paths = []
        self.visited = set()

    def traverse(self):
        self.paths = [(0,0,0,0,0,0)] # x, y, dx, dy, n, hl
        while self.paths:
            heat_loss, row, col, drow, dcol, n_steps = heappop(self.paths)

            if row == self.grid.shape[0] - 1 and col == self.grid.shape[1] - 1:
                return heat_loss

            if row < 0 or row >= self.grid.shape[0] or col < 0 or col >= self.grid.shape[1]:
                continue

            if (row, col, drow, dcol, n_steps) in self.visited:
                continue

            self.visited.add((row, col, drow, dcol, n_steps))

            if n_steps < 3 and (drow, dcol) != (0, 0):
                new_row = drow + row
                new_col = dcol + col
                if 0 <= new_row < self.grid.shape[0] and 0 <= new_col < self.grid.shape[1]:
                    heappush(self.paths, (heat_loss + self.grid[new_row, new_col], new_row, new_col, drow, dcol, n_steps + 1))
            
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for new_drow, new_dcol in dirs:
                
                if (new_drow, new_dcol) != (drow, dcol) and (new_drow, new_dcol) != (-drow, -dcol):
                    new_row = new_drow + row
                    new_col = new_dcol + col
                    if 0 <= new_row < self.grid.shape[0] and 0 <= new_col < self.grid.shape[1]:
                        heappush(self.paths, (heat_loss + self.grid[new_row, new_col], new_row, new_col, new_drow, new_dcol, 1))