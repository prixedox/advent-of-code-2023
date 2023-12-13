import numpy as np

class MirrorFinder:

    def __init__(self):
        pass

    def find_all(self, grids):
        total = 0
        for grid in grids:
            np_grid = np.array(grid)
            row = self.find_single_row(np_grid)
            col = self.find_single_col(np_grid)
            if row == None:
                row = 0
            if col == None:
                col = 0

            if row > col and col > 0:
                row = 0
            elif row <= col and row > 0:
                col = 0

            total += row * 100 + col

        return total

    def find_single_row(self, grid):      
        for i in range(0, len(grid) - 1):
            j = 0
            num_diff = 0
            while True:
                if i + j > len(grid) - 2 or i - j < 0:
                    if num_diff == 1:
                        return i + 1
                    break
                
                line1 = grid[i-j]
                line2 = grid[i + j + 1]
                num_diff += np.sum(line1 != line2)

                if num_diff > 1:
                    break
                
                j += 1

    
    def find_single_col(self, grid):        
        for i in range(0, len(grid[0]) - 1):
            j = 0
            num_diff = 0
            while True:
                if i + j + 1 > len(grid[0]) - 1 or i - j < 0:
                    if num_diff == 1:
                        return i + 1
                    break
                
                line1 = grid[:,i-j]
                line2 = grid[:,i + j + 1]
                num_diff += np.sum(line1 != line2)

                if num_diff > 1:
                    break

                j += 1